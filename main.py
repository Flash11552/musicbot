# main.py - Saski Telegram Bot (aiogram v3.x)
# Tam yenilenmis: dost oyunu inline fix, broadcast, bot stats xaric,
# ELO mesajlari, qrup deskteyi, heç-heçə/təslim düzgün axış.

import os
import asyncio
import functools
import random
import logging
import time

import uuid
from aiogram import Bot, Dispatcher, F, types
from aiogram.exceptions import TelegramRetryAfter
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

import database as db
import game_logic as gl
from locales import t

# ---------------------------------------------------------------------------
# Konfiqurasiya
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN .env faylinda tapilmadi!")

# Adminlər: .env-də  ADMIN_IDS=111,222,333
_admin_raw = os.getenv("ADMIN_IDS", "")
ADMIN_IDS: set = {int(x.strip()) for x in _admin_raw.split(",") if x.strip().isdigit()}

bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher()

MOVE_TIMEOUT = 60

# Aktiv taymerler: {game_id: asyncio.Task}
_timers: dict = {}


# ---------------------------------------------------------------------------
# Async DB köməkçisi — event loop-u bloklamır (qrup donmalarının həlli)
# ---------------------------------------------------------------------------

async def _db(fn, *args, **kwargs):
    """DB funksiyasını thread pool-da icra edir — qrup oyunlarında donmağı aradan qaldırır."""
    return await asyncio.to_thread(functools.partial(fn, *args, **kwargs))


# ---------------------------------------------------------------------------
# Köməkçilər
# ---------------------------------------------------------------------------

def _lang(user_id: int) -> str:
    if not user_id or user_id == 0:
        return "az"
    return db.get_user(user_id).get("lang") or "az"


def _remaining_sec(game: dict) -> int:
    if not game.get("last_move_time"):
        return MOVE_TIMEOUT
    elapsed = db.seconds_since(game["last_move_time"])
    return max(0, MOVE_TIMEOUT - int(elapsed))


import html

def _esc(text: str) -> str:
    """HTML xətalarının qarşısını almaq üçün xüsusi simvolları təmizləyir/qaçırır."""
    if not text:
        return ""
    return html.escape(text)

def _display_name(user_id, fallback: str = None) -> str:
    """Həmişə AD qaytarır — heç vaxt rəqəmsal ID göstərmir."""
    if user_id == 0 or user_id is None:
        return "Bot"
    name = db.get_username(user_id)
    if name and name != str(user_id):
        return _esc(name)
    return fallback or "Oyunçu"


def _elo_args(uid: int, delta: int) -> dict:
    """ELO mesajı üçün {old_elo, new_elo, delta} — update_stats ƏVVƏL çağrılmalıdır."""
    u   = db.get_user(uid)
    new = u.get("rating", 1000)
    old = max(100, new - delta)   # delta artıq tətbiq edilib
    return {"old_elo": old, "new_elo": new, "delta": abs(delta)}


# ---------------------------------------------------------------------------
# Oyun bitişi — hər iki tərəfə öz dilindəki mesaj
# ---------------------------------------------------------------------------

async def _send_game_over(game: dict, game_id: str,
                          winner_id: int, loser_id: int,
                          msg_w_key: str, msg_l_key: str,
                          inline_id=None,
                          wk: dict = None, lk: dict = None):
    p_white = game["player_white"]
    p_black = game["player_black"]
    lang_w  = _lang(p_white) if p_white else "az"
    lang_b  = _lang(p_black) if p_black and p_black != 0 else lang_w
    game_lang = game.get("game_lang")
    wk = wk or {}
    lk = lk or {}

    try:
        if inline_id:
            # Inline mesaj: tək mesaj, qalib dilinə görə
            lang_show = game_lang or (_lang(winner_id) if winner_id else lang_w)
            try:
                await bot.edit_message_text(
                    text=t(lang_show, msg_w_key, **wk),
                    inline_message_id=inline_id,
                    reply_markup=_board_markup(game["board"], game_id, lang_show, is_game_over=True),
                    parse_mode="HTML"
                )
            except Exception:
                pass
            # Hər iki oyunçuya şəxsi bildiriş
            for uid, mk, kw in [
                (p_white, msg_w_key if winner_id == p_white else msg_l_key, wk if winner_id == p_white else lk),
                (p_black, msg_w_key if winner_id == p_black else msg_l_key, wk if winner_id == p_black else lk),
            ]:
                if uid and uid != 0:
                    try:
                        await bot.send_message(uid, t(_lang(uid), mk, **kw), parse_mode="HTML")
                    except Exception:
                        pass
        elif game.get("shared_chat_id") and game.get("shared_msg_id"):
            # Shared mesaj (qrup /saski friend): tək mesaj, game_lang ilə
            lang_use = game_lang or lang_w
            txt_w = t(lang_use, msg_w_key, **wk) if winner_id == p_white else t(lang_use, msg_l_key, **lk)
            try:
                await bot.edit_message_text(
                    text=txt_w,
                    chat_id=game["shared_chat_id"],
                    message_id=game["shared_msg_id"],
                    reply_markup=_board_markup(game["board"], game_id, lang_use, is_game_over=True),
                    parse_mode="HTML"
                )
            except Exception:
                pass
            # Hər iki oyunçuya şəxsi bildiriş (mümkündürsə)
            for uid, mk, kw in [
                (p_white, msg_w_key if winner_id == p_white else msg_l_key,
                         wk if winner_id == p_white else lk),
                (p_black, msg_w_key if winner_id == p_black else msg_l_key,
                         wk if winner_id == p_black else lk),
            ]:
                if uid and uid != 0:
                    try:
                        await bot.send_message(
                            uid, t(_lang(uid), mk, **kw), parse_mode="HTML"
                        )
                    except Exception:
                        pass
        else:
            if game.get("white_chat_id") and game.get("white_msg_id"):
                txt_w = t(lang_w, msg_w_key, **wk) if winner_id == p_white else t(lang_w, msg_l_key, **lk)
                try:
                    await bot.edit_message_reply_markup(
                        chat_id=game["white_chat_id"],
                        message_id=game["white_msg_id"],
                        reply_markup=_board_markup(game["board"], game_id, lang_w, is_game_over=True)
                    )
                except Exception:
                    pass
                try:
                    await bot.send_message(
                        chat_id=game["white_chat_id"],
                        text=txt_w,
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
            if game.get("black_chat_id") and game.get("black_msg_id") and p_black and p_black != 0:
                txt_b = t(lang_b, msg_w_key, **wk) if winner_id == p_black else t(lang_b, msg_l_key, **lk)
                try:
                    await bot.edit_message_reply_markup(
                        chat_id=game["black_chat_id"],
                        message_id=game["black_msg_id"],
                        reply_markup=_board_markup(game["board"], game_id, lang_b, is_game_over=True)
                    )
                except Exception:
                    pass
                try:
                    await bot.send_message(
                        chat_id=game["black_chat_id"],
                        text=txt_b,
                        parse_mode="HTML"
                    )
                except Exception:
                    pass
    except Exception as e:
        logging.warning("_send_game_over: %s", e)


# ---------------------------------------------------------------------------
# Taymer
# ---------------------------------------------------------------------------

def _cancel_timer(game_id: str):
    task = _timers.pop(game_id, None)
    if task and not task.done():
        task.cancel()


def _start_timer(game_id: str, turn: str, player_id: int):
    _cancel_timer(game_id)
    _timers[game_id] = asyncio.create_task(
        _timeout_task(game_id, turn, player_id)
    )


async def _timeout_task(game_id: str, turn_started: str, player_id: int):
    await asyncio.sleep(MOVE_TIMEOUT)
    game = db.get_game(game_id)
    if not game or game["turn"] != turn_started:
        return

    p_white   = game["player_white"]
    p_black   = game["player_black"]
    game_type = game.get("game_type", "")
    inline_id = game.get("inline_msg_id")

    # Bot oyununda: kimin NÖVBƏSI olduğuna bax — o gəlməyib
    if game_type == "bot":
        current_turn = game["turn"]   # turn_started ilə eynidir (yoxlanıb)
        if current_turn == "black":
            # Bot gəlmədi → oyunçu qalib (ELO yoxdur)
            winner_id = p_white
            loser_id  = 0            # bot
        else:
            # Oyunçu gəlmədi → oyunçu məğlub (ELO yoxdur)
            winner_id = 0            # bot (məntiqən)
            loser_id  = p_white

        winner_name = _display_name(winner_id) if winner_id else "Bot"
        loser_name  = _display_name(loser_id)  if loser_id  else "Bot"
        _timers.pop(game_id, None)
        db.delete_game(game_id)

        if current_turn == "black":
            # Bot gəlmədi → oyunçu qazandı
            wk = {"winner": winner_name}
            lk = {"winner": winner_name}
            msg_w = msg_l = "timeout_winner_bot"
        else:
            # Oyunçu gəlmədi → oyunçu uduzdu
            wk = {"loser": loser_name}
            lk = {"loser": loser_name}
            msg_w = msg_l = "timeout_loser_bot"

        await _send_game_over(game, game_id, winner_id, loser_id,
                              msg_w, msg_l, inline_id, wk, lk)
        return

    # PvP / Friend oyunları — kimin növbəsi idi, o məğlubdur
    loser_id  = player_id
    winner_id = p_black if player_id == p_white else p_white

    winner_name = _display_name(winner_id)
    loser_name  = _display_name(loser_id)

    _timers.pop(game_id, None)
    db.delete_game(game_id)

    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and loser_id \
            and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old_elo"], "w_new": w_args["new_elo"], "w_diff": w_args["delta"],
            "l_old": l_args["old_elo"], "l_new": l_args["new_elo"], "l_diff": l_args["delta"],
            "w_icon": w_icon, "l_icon": l_icon
        }
        wk = elo_data
        lk = elo_data
        msg_w, msg_l = "timeout_winner", "timeout_loser"
    else:
        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        wk = {"winner": winner_name, "loser": loser_name, "w_icon": w_icon, "l_icon": l_icon}
        lk = {"winner": winner_name, "loser": loser_name, "w_icon": w_icon, "l_icon": l_icon}
        msg_w, msg_l = "timeout_winner_bot", "timeout_loser_bot" 

    await _send_game_over(game, game_id, winner_id, loser_id,
                          msg_w, msg_l, inline_id, wk, lk)


# ---------------------------------------------------------------------------
# Klaviatura
# ---------------------------------------------------------------------------

def _board_markup(board: list, game_id: str, lang: str, is_game_over: bool = False) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for r_idx, row in enumerate(board):
        for c_idx, cell in enumerate(row):
            if cell == " ":
                builder.button(text="\u2003", callback_data="noop")
            else:
                builder.button(text=cell, callback_data=f"cell_{game_id}_{r_idx}_{c_idx}")
    if not is_game_over:
        builder.button(text=t(lang, "btn_surrender"), callback_data=f"surrender_{game_id}")
        builder.button(text=t(lang, "btn_draw"),      callback_data=f"draw_offer_{game_id}")
    builder.adjust(*([8] * 8 + [2]))
    return builder.as_markup()


def _language_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🇦🇿 Azərbaycan", callback_data="lang_az")
    builder.button(text="🇷🇺 Русский",    callback_data="lang_ru")
    builder.button(text="🇬🇧 English",    callback_data="lang_en")
    builder.button(text="🇹🇷 Türkçe",     callback_data="lang_tr")
    builder.button(text="🇰🇿 Қазақша",    callback_data="lang_kk")
    builder.button(text="🇰🇬 Кыргызча",   callback_data="lang_ky")
    builder.button(text="🇮🇳 हिन्दी",       callback_data="lang_hi")
    builder.button(text="🇺🇿 O'zbekcha",  callback_data="lang_uz")
    builder.button(text="🇸🇦 العربية",     callback_data="lang_ar")
    builder.button(text="🇮🇩 Indonesia",  callback_data="lang_id")
    builder.button(text="🇱🇹 Lietuvių",   callback_data="lang_lt")
    builder.adjust(3)
    return builder.as_markup()


def _main_menu_keyboard(lang: str) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_profile"),     callback_data="menu_profile")
    builder.button(text=t(lang, "btn_bot"),         callback_data="menu_bot")
    builder.button(text=t(lang, "btn_online"),      callback_data="menu_online")
    builder.button(text=t(lang, "btn_friend"),      switch_inline_query="")
    builder.button(text=t(lang, "btn_rating"),      callback_data="menu_rating_top")
    builder.button(text=t(lang, "btn_other_bots"),  url="https://t.me/your_channel_here")
    builder.button(text=t(lang, "btn_add_group"),   url="https://t.me/SaskiGameBot?startgroup=true")
    builder.button(text=t(lang, "btn_change_lang"), callback_data="menu_change_language")
    builder.adjust(2, 2, 2, 2)
    return builder.as_markup()


def _game_status_text(game: dict, lang_display: str,
                      error_code: str = None, err_for_user: int = None) -> str:
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    game_type = game.get("game_type", "")

    white_name = _display_name(p_white)
    if game_type == "bot":
        black_name = t(lang_display, "bot_label")
    else:
        black_name = _display_name(p_black) if p_black else t(lang_display, "waiting_player")

    mode_map = {"bot": "mode_bot", "pvp": "mode_pvp",
                "friend": "mode_friend", "friend_group": "mode_friend",
                "friend_cmd": "mode_friend"}
    mode_str = t(lang_display, mode_map.get(game_type, "mode_pvp"))

    header = t(lang_display, "board_header", mode=mode_str, white=white_name, black=black_name)

    is_group = bool(
        game.get("inline_msg_id") or 
        game.get("shared_chat_id") or 
        (game.get("white_chat_id") and int(game.get("white_chat_id")) < 0)
    )
    if is_group:
        sec = 60
    else:
        sec = _remaining_sec(game)
    turn = game["turn"]
    if turn == "white":
        turn_str = t(lang_display, "turn_white", name=white_name, sec=sec)
    else:
        tp = t(lang_display, "bot_label") if game_type == "bot" else black_name
        turn_str = t(lang_display, "turn_black", name=tp, sec=sec)

    text = header + turn_str
    if error_code and err_for_user is not None and not is_group:
        text += "\n\n⚠️ *" + t(lang_display, error_code) + "*"
    return text


# ---------------------------------------------------------------------------
# Lövhəni hər iki oyuncuya göndər
# ---------------------------------------------------------------------------

import time

_edit_versions = {}
_rate_limits = {}

_last_edit_time = {}

async def _safe_edit(text: str, markup, chat_id=None, message_id=None, inline_message_id=None):
    key = inline_message_id if inline_message_id else f"{chat_id}_{message_id}"
    version = time.time()
    _edit_versions[key] = version

    kwargs = dict(text=text, reply_markup=markup, parse_mode="HTML")
    if inline_message_id:
        kwargs["inline_message_id"] = inline_message_id
    else:
        kwargs["chat_id"] = chat_id
        kwargs["message_id"] = message_id

    while True:
        if _edit_versions.get(key) != version:
            return
        try:
            await bot.edit_message_text(**kwargs)
            return
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
        except Exception:
            return


async def _push_board_to_both(game_id: str, error_code: str = None, err_for_user: int = None):
    game = await _db(db.get_game, game_id)  # to_thread: qrup donmağı aradan qaldırır
    if not game:
        return
    p_white = game["player_white"]
    p_black = game["player_black"]
    board   = game["board"]
    lang_g  = game.get("game_lang") or None  # shared language if set

    # --- Shared mesaj (qrup / /saski friend) ---
    if game.get("shared_chat_id") and game.get("shared_msg_id"):
        lang_use = lang_g or (_lang(p_white) if p_white else "az")
        await _safe_edit(
            text=_game_status_text(game, lang_use, error_code, err_for_user),
            markup=_board_markup(board, game_id, lang_use),
            chat_id=game["shared_chat_id"],
            message_id=game["shared_msg_id"]
        )
        return

    lang_w  = _lang(p_white) if p_white else "az"
    lang_b  = _lang(p_black) if p_black and p_black != 0 else lang_w

    if game.get("white_chat_id") and game.get("white_msg_id"):
        err_w = error_code if err_for_user == p_white else None
        await _safe_edit(
            text=_game_status_text(game, lang_w, err_w, p_white),
            markup=_board_markup(board, game_id, lang_w),
            chat_id=game["white_chat_id"],
            message_id=game["white_msg_id"]
        )

    if game.get("black_chat_id") and game.get("black_msg_id") and p_black and p_black != 0:
        err_b = error_code if err_for_user == p_black else None
        await _safe_edit(
            text=_game_status_text(game, lang_b, err_b, p_black),
            markup=_board_markup(board, game_id, lang_b),
            chat_id=game["black_chat_id"],
            message_id=game["black_msg_id"]
        )


async def _push_inline_board(game_id: str, inline_msg_id: str,
                              error_code: str = None, err_for_user: int = None):
    game = await _db(db.get_game, game_id)  # to_thread: inline qrup donmağı aradan qaldırır
    if not game:
        return
    lang_w = game.get("game_lang") or (_lang(game["player_white"]) if game["player_white"] else "az")
    try:
        await bot.edit_message_text(
            text=_game_status_text(game, lang_w, error_code, err_for_user),
            inline_message_id=inline_msg_id,
            reply_markup=_board_markup(game["board"], game_id, lang_w),
            parse_mode="HTML"
        )
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after + 0.5)
        try:
            await bot.edit_message_text(
                text=_game_status_text(game, lang_w, error_code, err_for_user),
                inline_message_id=inline_msg_id,
                reply_markup=_board_markup(game["board"], game_id, lang_w),
                parse_mode="HTML"
            )
        except Exception:
            pass
    except Exception as e:
        logging.warning("Inline board yenileme: %s", e)


# ---------------------------------------------------------------------------
# /start  — istifadəçi + qrup qeydiyyatı
# ---------------------------------------------------------------------------

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id   = message.from_user.id
    chat_id   = message.chat.id
    chat_type = message.chat.type
    name      = message.from_user.first_name or str(user_id)
    db.update_username(user_id, name)
    db.register_chat(user_id, "private", name)
    if chat_type in ("group", "supergroup"):
        db.register_chat(chat_id, chat_type, message.chat.title or "")

    user_data = db.get_user(user_id)
    if not user_data.get("lang"):
        await message.answer(t("az", "select_language"),
                             reply_markup=_language_keyboard(), parse_mode="HTML")
    else:
        lang = user_data["lang"]
        await message.answer(t(lang, "start_text"),
                             reply_markup=_main_menu_keyboard(lang), parse_mode="HTML")


@dp.message(Command("language"))
async def cmd_language(message: types.Message):
    db.update_username(message.from_user.id,
                       message.from_user.first_name or str(message.from_user.id))
    await message.answer(t("az", "select_language"),
                         reply_markup=_language_keyboard(), parse_mode="HTML")


# ---------------------------------------------------------------------------
# /saski — qısa oyun başlatma əmri (şəxsi + qrup)
# ---------------------------------------------------------------------------

@dp.message(Command("saski"))
async def cmd_saski(message: types.Message):
    user_id = message.from_user.id
    name    = message.from_user.first_name or "Oyunçu"
    db.update_username(user_id, name)
    lang = _lang(user_id)

    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "saski_cmd_bot_btn"),
                   callback_data=f"saskibot_{message.chat.id}_{user_id}")
    builder.button(text=t(lang, "saski_cmd_frnd_btn"),
                   callback_data=f"saskifrnd_{message.chat.id}_{user_id}")
    builder.adjust(2)

    await message.reply(
        t(lang, "saski_cmd_menu"),
        reply_markup=builder.as_markup(),
        parse_mode="HTML"
    )


@dp.callback_query(F.data.startswith("saskibot_"))
async def cb_saski_bot(callback: types.CallbackQuery):
    """Bot ilə oyun — /saski əmrindən."""
    parts   = callback.data[len("saskibot_"):].split("_", 1)
    chat_id = int(parts[0])
    user_id = int(parts[1])

    # Yalnız əmri verən oyunçu oynaya bilər
    if callback.from_user.id != user_id:
        await callback.answer()
        return

    name = callback.from_user.first_name or "Oyunçu"
    db.update_username(user_id, name)
    lang = _lang(user_id)

    # Paralel oyunlara icazə verir — hər oyunun unikal ID-si var
    game_id = f"bot_{user_id}_{str(uuid.uuid4())[:8]}"

    board = gl.create_initial_board()
    db.create_game(game_id, user_id, board, game_type="bot", player_black=0)
    db.update_username(0, "Bot")
    game_obj = db.get_game(game_id)

    try:
        msg = await callback.message.edit_text(
            t(lang, "bot_game_start") + _game_status_text(game_obj, lang),
            reply_markup=_board_markup(board, game_id, lang),
            parse_mode="HTML"
        )
        mid = msg.message_id
        cid = msg.chat.id
    except Exception:
        msg = await bot.send_message(
            chat_id,
            t(lang, "bot_game_start") + _game_status_text(game_obj, lang),
            reply_markup=_board_markup(board, game_id, lang),
            parse_mode="HTML"
        )
        mid = msg.message_id
        cid = chat_id

    db.update_game_msg_ids(game_id, white_chat_id=cid, white_msg_id=mid)
    _start_timer(game_id, "white", user_id)
    await callback.answer()


@dp.callback_query(F.data.startswith("saskifrnd_"))
async def cb_saski_friend_menu(callback: types.CallbackQuery):
    """Dost ilə oyun menyusu — /saski əmrindən. Rəng + dil seçimi."""
    parts   = callback.data[len("saskifrnd_"):].split("_", 1)
    chat_id = int(parts[0])
    creator_id = int(parts[1])

    user_id = callback.from_user.id
    name    = callback.from_user.first_name or "Oyunçu"
    db.update_username(user_id, name)
    lang = _lang(creator_id)  # yaradıcının dili ilə göstər

    # game_id: mesajın chat_id + message_id əsasında
    msg_id  = callback.message.message_id
    game_id = f"scmd_{chat_id}_{msg_id}"

    # Mövcud oyun yoxsa — yarat
    game = db.get_game(game_id)
    if not game:
        board = gl.create_initial_board()
        db.create_game(game_id, -(creator_id), board,
                       game_type="friend_cmd",
                       player_black=None, game_lang=lang)
        db.update_game_msg_ids(game_id,
                               shared_chat_id=chat_id,
                               shared_msg_id=msg_id)
        game = db.get_game(game_id)

    game_lang = game.get("game_lang") or lang
    wait      = t(game_lang, "group_waiting_color")
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    uw = p_white if (p_white and p_white > 0) else None
    ub = p_black if (p_black and p_black not in (None, 0)) else None
    wn = _display_name(uw) if uw else wait
    bn = _display_name(ub) if ub else wait

    markup = _scmd_color_markup(game_id, game_lang,
                                white_chosen=bool(uw),
                                black_chosen=bool(ub))
    try:
        await callback.message.edit_text(
            t(game_lang, "friend_pick_color_text", white=wn, black=bn),
            reply_markup=markup,
            parse_mode="HTML"
        )
    except Exception:
        pass
    await callback.answer()


def _scmd_color_markup(game_id: str, lang: str,
                       white_chosen: bool, black_chosen: bool) -> types.InlineKeyboardMarkup:
    """Rəng seçim klaviaturası — /saski friend (scmd) oyunları üçün."""
    builder = InlineKeyboardBuilder()
    if not white_chosen:
        builder.button(text=t(lang, "friend_join_white_btn"),
                       callback_data=f"scmdw_{game_id}")
    if not black_chosen:
        builder.button(text=t(lang, "friend_join_black_btn"),
                       callback_data=f"scmdb_{game_id}")
    builder.button(text=t(lang, "friend_lang_btn"),
                   callback_data=f"scmdlang_{game_id}")
    builder.adjust(1)
    return builder.as_markup()


@dp.callback_query(F.data.startswith("scmdw_") | F.data.startswith("scmdb_"))
async def cb_scmd_color(callback: types.CallbackQuery):
    """/saski friend — rəng seçimi."""
    data    = callback.data
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or "Oyunçu")
    lang = _lang(user_id)

    if data.startswith("scmdw_"):
        chosen_color = "white"
        game_id = data[len("scmdw_"):]
    else:
        chosen_color = "black"
        game_id = data[len("scmdb_"):]

    game = db.get_game(game_id)
    if not game:
        await callback.answer(t(lang, "err_game_not_found"), show_alert=True)
        return

    game_lang  = game.get("game_lang") or lang
    p_white    = game["player_white"]
    p_black    = game["player_black"]
    creator_id = -(p_white) if (p_white and p_white < 0) else None

    real_white = p_white if (p_white and p_white > 0) else None
    real_black = p_black if (p_black and p_black not in (None, 0)) else None

    # Hər iki oyunçu seçilib → oyun artıq başlamışdır
    if real_white and real_black:
        await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
        return

    # Bu şəxs artıq qoşulub — rəng keçidini yoxla
    if user_id in (real_white, real_black):
        if user_id == real_white:
            if real_black is None:
                db.update_game(game_id, game["board"], "white", None,
                               clear_player_white=True, player_black=user_id, update_move_time=False)
                await callback.answer(t(lang, "friend_you_black"))
            else:
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
        else:  # user_id == real_black
            if real_white is None:
                db.update_game(game_id, game["board"], "white", None,
                               player_white=user_id, clear_player_black=True, update_move_time=False)
                await callback.answer(t(lang, "friend_you_white"))
            else:
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
        # Keçiddən sonra mesajı yenilə
        updated2 = db.get_game(game_id)
        uw2 = updated2["player_white"] if updated2 else None
        ub2 = updated2["player_black"] if updated2 else None
        nw2 = uw2 if (uw2 and uw2 > 0) else None
        nb2 = ub2 if (ub2 and ub2 not in (None, 0)) else None
        if nw2 and nb2:
            await _launch_scmd_game(game_id, nw2, nb2,
                                    game.get("shared_chat_id"), game.get("shared_msg_id"), game.get("inline_msg_id"), game_lang)
        else:
            wait = t(game_lang, "group_waiting_color")
            wn2 = _display_name(nw2) if nw2 else wait
            bn2 = _display_name(nb2) if nb2 else wait
            mu2 = _scmd_color_markup(game_id, game_lang,
                                     white_chosen=bool(nw2), black_chosen=bool(nb2))
            await _safe_edit(
                text=t(game_lang, "friend_pick_color_text", white=wn2, black=bn2),
                markup=mu2,
                chat_id=game.get("shared_chat_id"),
                message_id=game.get("shared_msg_id"),
                inline_message_id=game.get("inline_msg_id")
            )
        return

    # Rəngi tətbiq et
    if chosen_color == "white":
        if real_white:
            await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
            return
        db.update_game(game_id, game["board"], "white", None,
                       player_white=user_id, update_move_time=False)
    else:
        if real_black:
            await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
            return
        db.update_game(game_id, game["board"], "white", None,
                       player_black=user_id, update_move_time=False)

    await callback.answer(
        t(lang, "friend_you_white" if chosen_color == "white" else "friend_you_black")
    )

    # Yenilənmiş oyunu al
    updated = db.get_game(game_id)
    uw = updated["player_white"] if updated else None
    ub = updated["player_black"] if updated else None
    new_white = uw if (uw and uw > 0) else None
    new_black = ub if (ub and ub not in (None, 0)) else None
    shared_cid = (updated or game).get("shared_chat_id")
    shared_mid = (updated or game).get("shared_msg_id")
    inline_id  = (updated or game).get("inline_msg_id")

    if new_white and new_black:
        # Oyunu başlat
        await _launch_scmd_game(game_id, new_white, new_black,
                                shared_cid, shared_mid, inline_id, game_lang)
    else:
        # Hələ gözlənilir — mesajı yenilə
        wait = t(game_lang, "group_waiting_color")
        wn = _display_name(new_white) if new_white else wait
        bn = _display_name(new_black) if new_black else wait
        markup = _scmd_color_markup(game_id, game_lang,
                                    white_chosen=bool(new_white),
                                    black_chosen=bool(new_black))
        await _safe_edit(
            text=t(game_lang, "friend_pick_color_text", white=wn, black=bn),
            markup=markup,
            chat_id=shared_cid, message_id=shared_mid,
            inline_message_id=inline_id
        )


@dp.callback_query(F.data.startswith("scmdlang_"))
async def cb_scmd_lang_select(callback: types.CallbackQuery):
    """/saski friend — dil seçim alt-klaviaturası."""
    game_id = callback.data[len("scmdlang_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return
    builder = InlineKeyboardBuilder()
    builder.button(text="🇦🇿 Azərbaycan", callback_data=f"scmdsetlang_{game_id}_az")
    builder.button(text="🇷🇺 Русский",    callback_data=f"scmdsetlang_{game_id}_ru")
    builder.button(text="🇬🇧 English",    callback_data=f"scmdsetlang_{game_id}_en")
    builder.button(text="🇹🇷 Türkçe",     callback_data=f"scmdsetlang_{game_id}_tr")
    builder.button(text="🇰🇿 Қазақша",    callback_data=f"scmdsetlang_{game_id}_kk")
    builder.button(text="🇰🇬 Кыргызча",   callback_data=f"scmdsetlang_{game_id}_ky")
    builder.button(text="🇮🇳 हिन्दी",       callback_data=f"scmdsetlang_{game_id}_hi")
    builder.button(text="🇺🇿 O'zbekcha",  callback_data=f"scmdsetlang_{game_id}_uz")
    builder.button(text="🇸🇦 العربية",     callback_data=f"scmdsetlang_{game_id}_ar")
    builder.button(text="🇮🇩 Indonesia",  callback_data=f"scmdsetlang_{game_id}_id")
    builder.button(text="🇱🇹 Lietuvių",   callback_data=f"scmdsetlang_{game_id}_lt")
    builder.adjust(3)
    await _safe_edit(
        text=t(game.get("game_lang") or "az", "friend_pick_color_title"),
        markup=builder.as_markup(),
        chat_id=game.get("shared_chat_id"), message_id=game.get("shared_msg_id"),
        inline_message_id=game.get("inline_msg_id")
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("scmdsetlang_"))
async def cb_scmd_set_lang(callback: types.CallbackQuery):
    """/saski friend — dili tətbiq et."""
    parts   = callback.data[len("scmdsetlang_"):].rsplit("_", 1)
    game_id = parts[0]
    chosen  = parts[1] if len(parts) == 2 else "az"
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return
    db.update_game(game_id, game["board"], game["turn"], game["selected_cell"],
                   game_lang=chosen, update_move_time=False)
    p_white = game["player_white"]
    p_black = game["player_black"]
    uw = p_white if (p_white and p_white > 0) else None
    ub = p_black if (p_black and p_black not in (None, 0)) else None
    wait = t(chosen, "group_waiting_color")
    wn = _display_name(uw) if uw else wait
    bn = _display_name(ub) if ub else wait
    markup = _scmd_color_markup(game_id, chosen,
                                white_chosen=bool(uw), black_chosen=bool(ub))
    await _safe_edit(
        text=t(chosen, "friend_pick_color_text", white=wn, black=bn),
        markup=markup,
        chat_id=game.get("shared_chat_id"), message_id=game.get("shared_msg_id"),
        inline_message_id=game.get("inline_msg_id")
    )
    await callback.answer(t(chosen, "group_lang_changed"), show_alert=True)


async def _launch_scmd_game(game_id: str, white_id: int, black_id: int,
                             shared_cid: int, shared_mid: int, inline_id: str, game_lang: str):
    """/saski friend: hər iki oyunçu seçdikdən sonra board göstər."""
    game_obj = db.get_game(game_id)
    if not game_obj:
        return
    board    = game_obj["board"]
    lang_use = game_lang or _lang(white_id)
    await _safe_edit(
        text=t(lang_use, "friend_game_starting") + "\n\n"
             + _game_status_text(game_obj, lang_use),
        markup=_board_markup(board, game_id, lang_use),
        chat_id=shared_cid, message_id=shared_mid, inline_message_id=inline_id
    )
    _start_timer(game_id, "white", white_id)


# Bot qrupa əlavə ediləndə qeydiyyat
@dp.my_chat_member()
async def on_chat_member_update(update: types.ChatMemberUpdated):
    chat = update.chat
    if update.new_chat_member.status in ("member", "administrator"):
        if chat.type in ("group", "supergroup"):
            db.register_chat(chat.id, chat.type, chat.title or "")


# ---------------------------------------------------------------------------
# /broadcast — yalnız adminlər
# ---------------------------------------------------------------------------

@dp.message(Command("broadcast"))
async def cmd_broadcast(message: types.Message):
    user_id = message.from_user.id
    lang    = _lang(user_id)

    if user_id not in ADMIN_IDS:
        await message.reply(t(lang, "broadcast_no_perm"))
        return
    if not message.reply_to_message:
        await message.reply(t(lang, "broadcast_no_reply"))
        return

    src     = message.reply_to_message
    chats   = db.get_all_chats()
    ok = fail = 0
    for cid in chats:
        try:
            await bot.forward_message(chat_id=cid,
                                      from_chat_id=src.chat.id,
                                      message_id=src.message_id)
            ok += 1
        except Exception:
            fail += 1
        await asyncio.sleep(0.05)
    await message.reply(t(lang, "broadcast_done", ok=ok, fail=fail))


# ---------------------------------------------------------------------------
# Dil
# ---------------------------------------------------------------------------

@dp.callback_query(F.data == "menu_change_language")
async def cb_change_lang(callback: types.CallbackQuery):
    await callback.message.edit_text(t("az", "select_language"),
                                     reply_markup=_language_keyboard(), parse_mode="HTML")
    await callback.answer()


@dp.callback_query(F.data.startswith("lang_"))
async def cb_save_language(callback: types.CallbackQuery):
    lang    = callback.data.split("_", 1)[1]
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or str(user_id))
    db.set_lang(user_id, lang)
    await callback.message.edit_text(
        text=t(lang, "start_text"), reply_markup=_main_menu_keyboard(lang), parse_mode="HTML"
    )
    await callback.answer(t(lang, "lang_selected"))


@dp.callback_query(F.data == "back_to_menu")
async def cb_back_home(callback: types.CallbackQuery):
    lang = _lang(callback.from_user.id)
    await callback.message.edit_text(
        text=t(lang, "start_text"), reply_markup=_main_menu_keyboard(lang), parse_mode="HTML"
    )
    await callback.answer()


# ---------------------------------------------------------------------------
# Profil
# ---------------------------------------------------------------------------

@dp.message(Command("my"))
async def cmd_my(message: types.Message):
    user_id = message.from_user.id
    db.update_username(user_id, message.from_user.first_name or str(user_id))
    lang  = _lang(user_id)
    u     = db.get_user(user_id)
    total = u.get("wins", 0) + u.get("losses", 0) + u.get("draws", 0)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_back"), callback_data="back_to_menu")
    await message.answer(
        text=t(lang, "profile_text",
               name=_esc(message.from_user.first_name or str(user_id)),
               elo=u["rating"], total_games=total,
               wins=u.get("wins", 0), losses=u.get("losses", 0), draws=u.get("draws", 0)),
        reply_markup=builder.as_markup(), parse_mode="HTML"
    )

@dp.callback_query(F.data == "menu_profile")
async def cb_profile(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or str(user_id))
    lang  = _lang(user_id)
    u     = db.get_user(user_id)
    total = u.get("wins", 0) + u.get("losses", 0) + u.get("draws", 0)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_back"), callback_data="back_to_menu")
    await callback.message.edit_text(
        text=t(lang, "profile_text",
               name=_esc(callback.from_user.first_name or str(user_id)),
               elo=u["rating"], total_games=total,
               wins=u.get("wins", 0), losses=u.get("losses", 0), draws=u.get("draws", 0)),
        reply_markup=builder.as_markup(), parse_mode="HTML"
    )
    await callback.answer()


# ---------------------------------------------------------------------------
# Kömək
# ---------------------------------------------------------------------------

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    user_id = message.from_user.id
    db.update_username(user_id, message.from_user.first_name or str(user_id))
    lang    = _lang(user_id)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_bot"),    callback_data="menu_bot")
    builder.button(text=t(lang, "btn_online"), callback_data="menu_online")
    builder.button(text=t(lang, "btn_rating"), callback_data="menu_rating_top")
    builder.button(text=t(lang, "btn_back"),   callback_data="back_to_menu")
    builder.adjust(2, 2)
    await message.answer(text=t(lang, "help_text"),
                         reply_markup=builder.as_markup(), parse_mode="HTML")
# ---------------------------------------------------------------------------
# Reytinq
# ---------------------------------------------------------------------------

@dp.message(Command("rating"))
async def cmd_rating(message: types.Message):
    lang = _lang(message.from_user.id)
    await _show_rating_menu(message.answer, lang)


@dp.callback_query(F.data == "menu_rating_top")
async def cb_rating_menu(callback: types.CallbackQuery):
    lang = _lang(callback.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_top_elo"),  callback_data="top_elo")
    builder.button(text=t(lang, "btn_top_wins"), callback_data="top_wins")
    builder.button(text=t(lang, "btn_back"),     callback_data="back_to_menu")
    builder.adjust(2, 1)
    await callback.message.edit_text(
        text=t(lang, "rating_menu"), reply_markup=builder.as_markup(), parse_mode="HTML"
    )
    await callback.answer()


async def _show_rating_menu(send_fn, lang: str):
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_top_elo"),  callback_data="top_elo")
    builder.button(text=t(lang, "btn_top_wins"), callback_data="top_wins")
    builder.button(text=t(lang, "btn_back"),     callback_data="back_to_menu")
    builder.adjust(2, 1)
    await send_fn(text=t(lang, "rating_menu"),
                  reply_markup=builder.as_markup(), parse_mode="HTML")


@dp.callback_query(F.data == "top_elo")
async def cb_top_elo(callback: types.CallbackQuery):
    lang = _lang(callback.from_user.id)
    rows = db.get_top_20_elo()
    text = t(lang, "top_elo_title")
    for idx, (uid, uname, rating) in enumerate(rows, 1):
        uname = _esc(uname) if uname else "Oyunçu"
        text += t(lang, "rating_row_elo", idx=idx, name=uname, val=rating)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_back"), callback_data="menu_rating_top")
    await callback.message.edit_text(text=text, reply_markup=builder.as_markup(), parse_mode="HTML")
    await callback.answer()


@dp.callback_query(F.data == "top_wins")
async def cb_top_wins(callback: types.CallbackQuery):
    lang = _lang(callback.from_user.id)
    rows = db.get_top_20_wins()
    text = t(lang, "top_wins_title")
    for idx, (uid, uname, wins) in enumerate(rows, 1):
        uname = _esc(uname) if uname else "Oyunçu"
        text += t(lang, "rating_row_wins", idx=idx, name=uname, val=wins)
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_back"), callback_data="menu_rating_top")
    await callback.message.edit_text(text=text, reply_markup=builder.as_markup(), parse_mode="HTML")
    await callback.answer()


# ---------------------------------------------------------------------------
# Onlayn eşləşmə
# ---------------------------------------------------------------------------

@dp.callback_query(F.data == "menu_online")
async def cb_online_search(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or str(user_id))
    lang = _lang(user_id)

    opponent_id = db.get_queue_opponent(user_id)
    if opponent_id:
        game_id  = f"pvp_{user_id}_{opponent_id}"
        board    = gl.create_initial_board()
        db.create_game(game_id, user_id, board, game_type="pvp", player_black=opponent_id)
        lang_b   = _lang(opponent_id)
        game_obj = db.get_game(game_id)

        msg_w = await bot.send_message(
            user_id,
            t(lang, "match_found_white") + _game_status_text(game_obj, lang),
            reply_markup=_board_markup(board, game_id, lang), parse_mode="HTML"
        )
        msg_b = await bot.send_message(
            opponent_id,
            t(lang_b, "match_found_black") + _game_status_text(game_obj, lang_b),
            reply_markup=_board_markup(board, game_id, lang_b), parse_mode="HTML"
        )
        db.update_game_msg_ids(
            game_id,
            white_chat_id=user_id,     white_msg_id=msg_w.message_id,
            black_chat_id=opponent_id, black_msg_id=msg_b.message_id
        )
        _start_timer(game_id, "white", user_id)
        await callback.answer()
    else:
        if db.add_to_queue(user_id):
            builder = InlineKeyboardBuilder()
            builder.button(text=t(lang, "cancel_search_btn"), callback_data="cancel_search")
            await callback.message.edit_text(
                text=t(lang, "searching"),
                reply_markup=builder.as_markup(), parse_mode="HTML"
            )
        else:
            await callback.answer(t(lang, "already_searching"), show_alert=True)


@dp.callback_query(F.data == "cancel_search")
async def cb_cancel_search(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.leave_queue(user_id)
    lang = _lang(user_id)
    await callback.message.edit_text(
        t(lang, "info"), reply_markup=_main_menu_keyboard(lang), parse_mode="HTML"
    )
    await callback.answer(t(lang, "search_cancelled"))


# ---------------------------------------------------------------------------
# Bot ilə oyun
# ---------------------------------------------------------------------------

@dp.callback_query(F.data == "menu_bot")
async def cb_bot_game(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or str(user_id))
    lang    = _lang(user_id)

    # Unikal game_id — paralel oyunlara icazə verir
    game_id = f"bot_{user_id}_{str(uuid.uuid4())[:8]}"
    board = gl.create_initial_board()
    db.create_game(game_id, user_id, board, game_type="bot", player_black=0)
    db.update_username(0, "Bot")

    game_obj = db.get_game(game_id)
    msg = await callback.message.answer(
        t(lang, "bot_game_start") + _game_status_text(game_obj, lang),
        reply_markup=_board_markup(board, game_id, lang), parse_mode="HTML"
    )
    db.update_game_msg_ids(game_id,
                           white_chat_id=callback.message.chat.id,
                           white_msg_id=msg.message_id)
    _start_timer(game_id, "white", user_id)
    await callback.answer()


# ---------------------------------------------------------------------------
# Dost ilə oyun — Inline
#
# game_id = f"friend_{user_id}_{uuid.uuid4()[:8]}" 
# chosen_inline_result → inline_message_id + chat_type məlum olur → DB-ə qeyd edilir.
# Şəxsi chat: birinci klik → gözləmə; ikinci klik → oyun başlayır.
# Qrup: rəng seçim mesajı göstərilir, hər oyunçu öz rəngini seçir; dil dəyişdirilə bilər.
# ---------------------------------------------------------------------------

def _group_color_markup(game_id: str, lang: str,
                        white_chosen: bool, black_chosen: bool) -> types.InlineKeyboardMarkup:
    """Qrup rəng seçim klaviaturası — seçilmiş rənglər passiv olur."""
    builder = InlineKeyboardBuilder()
    if not white_chosen:
        builder.button(text=t(lang, "friend_join_white_btn"),
                       callback_data=f"fjoin_w_{game_id}")
    if not black_chosen:
        builder.button(text=t(lang, "friend_join_black_btn"),
                       callback_data=f"fjoin_b_{game_id}")
    builder.button(text=t(lang, "group_select_lang_btn"),
                   callback_data=f"gflang_{game_id}")
    builder.adjust(1)
    return builder.as_markup()


async def _refresh_group_color_msg(game_id: str, inline_msg_id: str, lang: str,
                                   white_name: str, black_name: str):
    """Qrup rəng seçim mesajını yenilə."""
    wait = t(lang, "group_waiting_color")
    w_display = white_name or wait
    b_display = black_name or wait
    white_chosen = bool(white_name)
    black_chosen = bool(black_name)
    text = t(lang, "group_color_select_msg", white=w_display, black=b_display)
    await _safe_edit(
        text=text,
        markup=_group_color_markup(game_id, lang, white_chosen, black_chosen),
        inline_message_id=inline_msg_id
    )


@dp.inline_query()
async def inline_handler(query: types.InlineQuery):
    """Inline sorğu — dil yoxlaması, t() ilə lokallaşdırılmış kart.
    İstifadəçinin dili yoxdursa → botda /start etməsinə yönləndir."""
    user_id = query.from_user.id
    import uuid
    game_id = f"friend_{user_id}_{str(uuid.uuid4())[:8]}"
    logging.info("INLINE_QUERY user_id=%s query=%r game_id=%s", user_id, query.query, game_id)

    lang = _lang(user_id)  # DB-dən istifadəçi dili

    # Dil seçilməyibsə → bota yönləndir
    if not lang or lang not in ("az", "ru", "en"):
        lang = "az"  # fallback göstərmək üçün
        no_lang_btn = InlineKeyboardBuilder()
        no_lang_btn.button(
            text=t(lang, "inline_no_lang_btn"),
            url="https://t.me/SaskiGameBot?start=setlang"
        )
        await query.answer(
            [
                types.InlineQueryResultArticle(
                    id="no_lang",
                    title=t(lang, "inline_title"),
                    description=t(lang, "inline_no_lang_msg"),
                    input_message_content=types.InputTextMessageContent(
                        message_text=t(lang, "inline_no_lang_msg"),
                        parse_mode="HTML"
                    ),
                    reply_markup=no_lang_btn.as_markup()
                )
            ],
            cache_time=0,
            is_personal=True
        )
        return

    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "saski_cmd_bot_btn"),    callback_data=f"imenu_bot_{game_id}")
    builder.button(text=t(lang, "saski_cmd_frnd_btn"), callback_data=f"imenu_frnd_{game_id}")
    builder.adjust(2)

    await query.answer(
        [
            types.InlineQueryResultArticle(
                id=game_id,
                title=t(lang, "inline_title"),
                description=t(lang, "inline_desc"),
                input_message_content=types.InputTextMessageContent(
                    message_text=t(lang, "saski_cmd_menu"),
                    parse_mode="HTML"
                ),
                reply_markup=builder.as_markup()
            )
        ],
        cache_time=0,
        is_personal=True
    )


@dp.chosen_inline_result()
async def on_chosen_inline_result(result: types.ChosenInlineResult):
    """İstifadəçi inline kartı seçdi → inline_message_id DB-ə yazılır."""
    game_id       = result.result_id
    inline_msg_id = result.inline_message_id
    creator_id    = result.from_user.id
    user_name     = result.from_user.first_name or "Oyunçu"
    logging.info("CHOSEN_INLINE game_id=%s inline_msg_id=%s creator=%s",
                 game_id, inline_msg_id, creator_id)

    if not inline_msg_id:
        logging.warning("CHOSEN_INLINE: inline_msg_id yoxdur, chosen_inline_result feedback aktiv deyil?")
        return

    is_group     = getattr(result, "chat_type", None) in ("group", "supergroup")
    gtype        = "friend_group" if is_group else "friend"
    creator_lang = _lang(creator_id)

    # İstifadəçini DB-yə qeyd et
    db.update_username(creator_id, user_name)

    old = db.get_game(game_id)
    if old:
        _cancel_timer(game_id)
        db.delete_game(game_id)

    board = gl.create_initial_board()
    db.create_game(game_id, -(creator_id), board,
                   game_type=gtype, player_black=None,
                   game_lang=creator_lang)
    db.update_game_msg_ids(game_id, inline_msg_id=inline_msg_id)
    logging.info("CHOSEN_INLINE: oyun yaradıldı game_id=%s gtype=%s", game_id, gtype)


@dp.callback_query(F.data.startswith("imenu_bot_") | F.data.startswith("imenu_frnd_"))
async def cb_inline_menu(callback: types.CallbackQuery):
    """Inline menyudan Bot|Dost seçimi."""
    data    = callback.data
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or "Oyunçu")
    lang = _lang(user_id)

    if data.startswith("imenu_bot_"):
        game_id = data[len("imenu_bot_"):]
        action  = "bot"
    else:
        game_id = data[len("imenu_frnd_"):]
        action  = "friend"

    game = db.get_game(game_id)
    inline_id = callback.inline_message_id or (game.get("inline_msg_id") if game else None)
    is_group  = (game.get("game_type") == "friend_group") if game else False
    game_lang = (game.get("game_lang") or lang) if game else lang

    if action == "bot":
        # Bot ilə oyna — unikal game_id; inline mesajı lövhəyə çevir
        ts         = int(time.time())
        bot_gid    = f"bot_{user_id}_{ts}"
        board      = gl.create_initial_board()
        db.create_game(bot_gid, user_id, board, game_type="bot", player_black=0)
        db.update_username(0, "Bot")
        if inline_id:
            db.update_game_msg_ids(bot_gid, inline_msg_id=inline_id)
        game_obj = db.get_game(bot_gid)
        if inline_id:
            try:
                await bot.edit_message_text(
                    text=t(lang, "bot_game_start") + "\n\n" + _game_status_text(game_obj, lang),
                    inline_message_id=inline_id,
                    reply_markup=_board_markup(board, bot_gid, lang),
                    parse_mode="HTML"
                )
            except Exception as e:
                logging.warning("imenu_bot edit: %s", e)
        # Köhnə "menu" oyunu sil
        if game:
            db.delete_game(game_id)
        _start_timer(bot_gid, "white", user_id)
        await callback.answer()

    else:  # friend
        if not game:
            # chosen_inline_result gəlməyib (inline feedback 0% ola bilər) — game-i lazy yarat
            if not inline_id:
                await callback.answer(t(lang, "err_game_not_found"), show_alert=True)
                return
            board_new = gl.create_initial_board()
            db.create_game(game_id, -(user_id), board_new,
                           game_type="friend_group", player_black=None,
                           game_lang=lang)
            db.update_game_msg_ids(game_id, inline_msg_id=inline_id)
            game      = db.get_game(game_id)

        game_lang = game.get("game_lang") or lang
        wait      = t(game_lang, "group_waiting_color")
        p_white   = game.get("player_white")
        p_black   = game.get("player_black")
        uw = p_white if (p_white and p_white > 0) else None
        ub = p_black if (p_black and p_black not in (None, 0)) else None
        wn = _display_name(uw) if uw else wait
        bn = _display_name(ub) if ub else wait

        markup = _scmd_color_markup(game_id, game_lang, white_chosen=bool(uw), black_chosen=bool(ub))
        
        await _safe_edit(
            text=t(game_lang, "friend_pick_color_text", white=wn, black=bn),
            markup=markup,
            inline_message_id=inline_id
        )
        await callback.answer()


@dp.callback_query(F.data.startswith("fjoin_w_") | F.data.startswith("fjoin_b_"))
async def cb_friend_join(callback: types.CallbackQuery):
    data    = callback.data
    user_id = callback.from_user.id
    user_name = callback.from_user.first_name or "Oyunçu"
    db.update_username(user_id, user_name)
    lang  = _lang(user_id)

    if data.startswith("fjoin_w_"):
        chosen_color = "white"
        game_id = data[len("fjoin_w_"):]
    else:
        chosen_color = "black"
        game_id = data[len("fjoin_b_"):]

    cb_inline_id = callback.inline_message_id
    game = db.get_game(game_id)
    is_group = (game.get("game_type") == "friend_group") if game else False
    game_lang = (game.get("game_lang") or lang) if game else lang

    # Oyun yoxdursa — chosen_inline_result hələ gəlməyib (nadir race)
    if game is None:
        board = gl.create_initial_board()
        if chosen_color == "white":
            db.create_game(game_id, user_id, board, game_type="friend", player_black=None)
        else:
            db.create_game(game_id, -(user_id), board, game_type="friend", player_black=user_id)
        if cb_inline_id:
            db.update_game_msg_ids(game_id, inline_msg_id=cb_inline_id)
        await _show_waiting_inline(game_id, user_id, chosen_color, cb_inline_id, lang)
        await callback.answer(
            t(lang, "friend_you_white" if chosen_color == "white" else "friend_you_black")
        )
        return

    p_white      = game["player_white"]
    p_black      = game["player_black"]
    saved_inline = game.get("inline_msg_id") or cb_inline_id

    if cb_inline_id and not game.get("inline_msg_id"):
        db.update_game_msg_ids(game_id, inline_msg_id=cb_inline_id)
        saved_inline = cb_inline_id

    creator_id = -(p_white) if (p_white and p_white < 0) else None

    # Özü ilə oynamaq qadağandır
    if creator_id and user_id == creator_id and not is_group:
        await callback.answer(t(lang, "friend_self_join"), show_alert=True)
        return

    real_white = p_white if (p_white and p_white > 0) else None
    real_black = p_black if (p_black and p_black not in (None, 0)) else None

    # Hər iki oyunçu artıq var → oyun başlamışdır
    if real_white and real_black:
        await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
        return

    # Bu oyunçu artıq qoşulub — rəng keçidini yoxla
    if user_id in (real_white, real_black):
        if user_id == real_white:
            if real_black is None:
                db.update_game(game_id, game["board"], "white", None,
                               clear_player_white=True, player_black=user_id, update_move_time=False)
                await callback.answer(t(lang, "friend_you_black"))
            else:
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
        else:  # user_id == real_black
            if real_white is None:
                db.update_game(game_id, game["board"], "white", None,
                               player_white=user_id, clear_player_black=True, update_move_time=False)
                await callback.answer(t(lang, "friend_you_white"))
            else:
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
        
        # Keçiddən sonra mesajı yenilə
        updated = db.get_game(game_id)
        uw = updated["player_white"] if updated else None
        ub = updated["player_black"] if updated else None
        new_white = uw if (uw and uw > 0) else None
        new_black = ub if (ub and ub not in (None, 0)) else None

        if is_group:
            if new_white and new_black:
                await _launch_friend_game(game_id, new_white, new_black,
                                          saved_inline, game_lang=game_lang)
            else:
                wn = _display_name(new_white) if new_white else None
                bn = _display_name(new_black) if new_black else None
                await _refresh_group_color_msg(game_id, saved_inline, game_lang, wn, bn)
        else:
            # Şəxsi chat: rəng dəyişdikdən sonra interfeysi yenilə
            new_color = "white" if new_white == user_id else "black"
            await _show_waiting_inline(game_id, user_id, new_color, saved_inline, game_lang)
        return

        if is_group:
            if new_white and new_black:
                await _launch_friend_game(game_id, new_white, new_black,
                                          saved_inline, game_lang=game_lang)
            else:
                wn = _display_name(new_white) if new_white else None
                bn = _display_name(new_black) if new_black else None
                await _refresh_group_color_msg(game_id, saved_inline, game_lang, wn, bn)
        else:
            # Şəxsi chat: rəng dəyişdikdən sonra interfeysi yenilə
            new_color = "white" if new_white == user_id else "black"
            await _show_waiting_inline(game_id, user_id, new_color, saved_inline, game_lang)
        return

    # ---------------------------------------------------------------
    # QRUP REJIMI — hər oyunçu öz rəngini ayrıca seçir
    # ---------------------------------------------------------------
    if is_group:
        if chosen_color == "white":
            if real_white:
                # Başqası tərəfindən seçilib
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
            # Ağ boşdur, bu oyunçu seçir
            db.update_game(game_id, game["board"], "white", None,
                           player_white=user_id, update_move_time=False)
            await callback.answer(t(lang, "friend_you_white"))
        else:  # black
            if real_black:
                await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
                return
            db.update_game(game_id, game["board"], "white", None,
                           player_black=user_id, update_move_time=False)
            await callback.answer(t(lang, "friend_you_black"))

        # Yenilənmiş oyunu yenidən al
        updated = db.get_game(game_id)
        uw = updated["player_white"] if updated else None
        ub = updated["player_black"] if updated else None
        new_white = uw if (uw and uw > 0) else None
        new_black = ub if (ub and ub not in (None, 0)) else None

        if new_white and new_black:
            # Hər iki rəng seçildi → oyunu başlat
            await _launch_friend_game(game_id, new_white, new_black,
                                      saved_inline, game_lang=game_lang)
        else:
            # Hələ gözlənilir → mesajı yenilə
            wn = _display_name(new_white) if new_white else None
            bn = _display_name(new_black) if new_black else None
            await _refresh_group_color_msg(game_id, saved_inline, game_lang, wn, bn)
        return

    # ---------------------------------------------------------------
    # ŞƏXSİ CHAT REJİMİ
    # ---------------------------------------------------------------
    # Gözləmə vəziyyəti: creator_id var, hər iki xana boşdur
    if creator_id and real_white is None and real_black is None:
        if chosen_color == "white":
            new_white, new_black = user_id, creator_id
        else:
            new_white, new_black = creator_id, user_id
        db.update_game(game_id, game["board"], "white", None,
                       player_white=new_white, player_black=new_black)
        await _launch_friend_game(game_id, new_white, new_black, saved_inline)
        await callback.answer(t(lang, "friend_game_starting"))
        return

    # Creator ağı seçmişdi → qara gözlənilir
    if real_white and real_black is None:
        if chosen_color == "black":
            db.update_game(game_id, game["board"], "white", None, player_black=user_id)
            await _launch_friend_game(game_id, real_white, user_id, saved_inline)
            await callback.answer(t(lang, "friend_game_starting"))
        else:
            await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
        return

    # Creator qaranı seçmişdi → ağ gözlənilir
    if real_black and real_white is None:
        if chosen_color == "white":
            db.update_game(game_id, game["board"], "white", None,
                           player_white=user_id, player_black=real_black)
            await _launch_friend_game(game_id, user_id, real_black, saved_inline)
            await callback.answer(t(lang, "friend_game_starting"))
        else:
            await callback.answer(t(lang, "friend_color_taken"), show_alert=True)
        return

    await callback.answer(t(lang, "friend_color_taken"), show_alert=True)


# ---------------------------------------------------------------------------
# Qrup oyununda dil seçimi
# ---------------------------------------------------------------------------

@dp.callback_query(F.data.startswith("gflang_"))
async def cb_group_lang_select(callback: types.CallbackQuery):
    """🌍 düyməsi: dil seçim alt-klaviaturasını göstər."""
    game_id = callback.data[len("gflang_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return
    lang = _lang(callback.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.button(text="🇦🇿 Azərbaycan", callback_data=f"gfsetlang_{game_id}_az")
    builder.button(text="🇷🇺 Русский",    callback_data=f"gfsetlang_{game_id}_ru")
    builder.button(text="🇬🇧 English",    callback_data=f"gfsetlang_{game_id}_en")
    builder.button(text="🇹🇷 Türkçe",     callback_data=f"gfsetlang_{game_id}_tr")
    builder.button(text="🇰🇿 Қазақша",    callback_data=f"gfsetlang_{game_id}_kk")
    builder.button(text="🇰🇬 Кыргызча",   callback_data=f"gfsetlang_{game_id}_ky")
    builder.button(text="🇮🇳 हिन्दी",       callback_data=f"gfsetlang_{game_id}_hi")
    builder.button(text="🇺🇿 O'zbekcha",  callback_data=f"gfsetlang_{game_id}_uz")
    builder.button(text="🇸🇦 العربية",     callback_data=f"gfsetlang_{game_id}_ar")
    builder.button(text="🇮🇩 Indonesia",  callback_data=f"gfsetlang_{game_id}_id")
    builder.button(text="🇱🇹 Lietuvių",   callback_data=f"gfsetlang_{game_id}_lt")
    builder.adjust(3)
    inline_id = callback.inline_message_id or game.get("inline_msg_id")
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    uw = p_white if (p_white and p_white > 0) else None
    ub = p_black if (p_black and p_black not in (None, 0)) else None
    game_lang = game.get("game_lang") or lang
    wait = t(game_lang, "group_waiting_color")
    text = t(game_lang, "group_color_select_msg",
             white=_display_name(uw) if uw else wait,
             black=_display_name(ub) if ub else wait)
    try:
        await bot.edit_message_text(
            text=text, inline_message_id=inline_id,
            reply_markup=builder.as_markup(), parse_mode="HTML"
        )
    except Exception:
        pass
    await callback.answer()


@dp.callback_query(F.data.startswith("gfsetlang_"))
async def cb_group_set_lang(callback: types.CallbackQuery):
    """Qrup oyunu üçün dil seç və mesajı yenilə."""
    parts   = callback.data[len("gfsetlang_"):].rsplit("_", 1)
    game_id = parts[0]
    chosen  = parts[1] if len(parts) == 2 else "az"
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return
    db.update_game(game_id, game["board"], game["turn"], game["selected_cell"],
                   game_lang=chosen, update_move_time=False)
    p_white = game["player_white"]
    p_black = game["player_black"]
    uw = p_white if (p_white and p_white > 0) else None
    ub = p_black if (p_black and p_black not in (None, 0)) else None
    inline_id = callback.inline_message_id or game.get("inline_msg_id")
    wn = _display_name(uw) if uw else None
    bn = _display_name(ub) if ub else None
    await _refresh_group_color_msg(game_id, inline_id, chosen, wn, bn)
    await callback.answer(t(chosen, "group_lang_changed"), show_alert=True)



# ---------------------------------------------------------------------------
# Dost oyunu köməkçiləri (_show_waiting_inline, _launch_friend_game)
# ---------------------------------------------------------------------------

async def _show_waiting_inline(game_id: str, user_id: int, chosen_color: str,
                                inline_msg_id, lang: str):
    """Şəxsi chat inline: gözləmə mesajını yenilə — qalan rəng düyməsini göstər."""
    if not inline_msg_id:
        return
    builder = InlineKeyboardBuilder()
    if chosen_color == "white":
        builder.button(text=t(lang, "friend_join_black_btn"),
                       callback_data=f"fjoin_b_{game_id}")
    else:
        builder.button(text=t(lang, "friend_join_white_btn"),
                       callback_data=f"fjoin_w_{game_id}")
    builder.adjust(1)
    chosen_key = "friend_you_white" if chosen_color == "white" else "friend_you_black"
    status = t(lang, "friend_waiting_msg") + "\n\n" + t(lang, chosen_key)
    try:
        await bot.edit_message_text(
            text=status, inline_message_id=inline_msg_id,
            reply_markup=builder.as_markup(), parse_mode="HTML"
        )
    except Exception as e:
        logging.warning("_show_waiting_inline: %s", e)


async def _launch_friend_game(game_id: str, white_id: int, black_id: int,
                               inline_msg_id, game_lang: str = None):
    """Inline dost oyunu: hər iki oyunçu müəyyənləşdikdən sonra lövhəni göstər.
    game_lang: qrup oyununda seçilmiş dil (None → white oyunçusunun dili)."""
    game_obj = db.get_game(game_id)
    if not game_obj:
        return
    if not inline_msg_id:
        logging.warning("_launch_friend_game: inline_msg_id yoxdur, oyun başlamadı!")
        return
    board    = game_obj["board"]
    lang_use = game_lang or game_obj.get("game_lang") or _lang(white_id)
    await _safe_edit(
        text=t(lang_use, "friend_game_starting") + "\n\n"
             + _game_status_text(game_obj, lang_use),
        markup=_board_markup(board, game_id, lang_use),
        inline_message_id=inline_msg_id
    )
    _start_timer(game_id, "white", white_id)


# ---------------------------------------------------------------------------
# Xana kliki — əsas oyun məntiqi
# ---------------------------------------------------------------------------


async def _bot_move_task_handler(game_id, current_board, inline_id):
    try:
        # First refresh to show the player's move
        if inline_id:
            await _push_inline_board(game_id, inline_id, None, None)
        else:
            await _push_board_to_both(game_id, None, None)
            
        await asyncio.sleep(0.4)
        
        # Now execute bot's move
        new_board = _execute_bot_turn(current_board)
        after_bot = gl.check_win_condition(new_board)
        
        game = db.get_game(game_id)
        if not game: return
        
        if after_bot:
            # We need to simulate _finish_game
            # But _finish_game requires callback.
            # It's better to inline the finish logic here for bot games.
            p_white = game["player_white"]
            winner_id = p_white if after_bot == "white" else 0
            loser_id  = 0 if after_bot == "white" else p_white
            winner_name = _display_name(winner_id)
            loser_name = _display_name(loser_id)
            _timers.pop(game_id, None)
            db.delete_game(game_id)
            wk = {"winner": winner_name, "loser": loser_name}
            lk = {"winner": winner_name, "loser": loser_name}
            await _send_game_over(game, game_id, winner_id, loser_id,
                                  "game_over_winner_bot", "game_over_loser_bot", inline_id, wk, lk)
            return

        db.update_game(game_id, new_board, "white", None, error_msg=None, err_recipient=None, update_move_time=True)
        _start_timer(game_id, "white", game["player_white"])
        
        if inline_id:
            await _push_inline_board(game_id, inline_id, None, None)
        else:
            await _push_board_to_both(game_id, None, None)
            
    except Exception as e:
        logging.warning("Bot move task error: %s", e)


@dp.callback_query(F.data.startswith("cell_"))
async def cb_cell_click(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_username(user_id, callback.from_user.first_name or str(user_id))

    parts   = callback.data.split("_")
    r       = int(parts[-2])
    c       = int(parts[-1])
    game_id = "_".join(parts[1:-2])

    game = await _db(db.get_game, game_id)  # to_thread: qrup callback donmağı aradan qaldırır
    if not game:
        await callback.answer("❓ Oyun tapılmadı.", show_alert=True)
        return

    board     = [row[:] for row in game["board"]]
    turn      = game["turn"]
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    selected  = game["selected_cell"]
    game_type = game["game_type"]
    lang      = _lang(user_id)
    inline_id = callback.inline_message_id or game.get("inline_msg_id")

    async def _refresh(err_code=None, err_user=None):
        if inline_id:
            await _push_inline_board(game_id, inline_id, err_code, err_user)
        else:
            await _push_board_to_both(game_id, err_code, err_user)
    if p_white and p_white < 0:
        await callback.answer()
        return

    # İştirakçı yoxlaması
    if user_id not in [p_white, p_black]:
        await callback.answer(t(lang, "not_participant"), show_alert=True)
        return

    # Növbə yoxlaması
    current_player = p_white if turn == "white" else p_black
    if user_id != current_player:
        await callback.answer(t(lang, "err_not_your_turn"), show_alert=True)
        return

    clicked   = board[r][c]
    my_tokens = (
        {gl.WHITE_MAN, gl.WHITE_KING} if turn == "white"
        else {gl.BLACK_MAN, gl.BLACK_KING}
    )

    # --- Daş seçimi ---
    if clicked in my_tokens or clicked == gl.SELECTED_MARK:
        if selected:
            prev_token = game.get("last_token_type")
            if prev_token and 0 <= selected[0] < 8 and 0 <= selected[1] < 8:
                board[selected[0]][selected[1]] = prev_token
        real_token = clicked if clicked != gl.SELECTED_MARK else game.get("last_token_type")
        board[r][c] = gl.SELECTED_MARK
        await _db(db.update_game, game_id, board, turn, [r, c],
                       last_token_type=real_token,
                       error_msg=None, err_recipient=None,
                       update_move_time=False)
        
        await callback.answer(t(lang, "piece_selected") or "✅")
        asyncio.create_task(_refresh())
        return

    # --- Hərəkət ---
    if selected and clicked == gl.EMPTY_DARK:
        from_pos   = (selected[0], selected[1])
        to_pos     = (r, c)
        real_token = game.get("last_token_type") or (
            gl.WHITE_MAN if turn == "white" else gl.BLACK_MAN
        )
        board[from_pos[0]][from_pos[1]] = real_token

        result = gl.validate_and_execute_move(board, from_pos, to_pos, turn)

        if result["status"] == "error":
            # The board state hasn't actually changed in the DB.
            # Just show the popup and return to avoid rate limits!
            await callback.answer(t(lang, result["reason"]), show_alert=True)
            return

        new_board = result["board"]

        # Ardıcıl yeymə məcburidir: eyni daşla davam et, xatırla
        if result.get("chain_possible"):
            # Dama olub + zəncir: xüsusi mesaj göstər
            err_msg = "err_king_promoted_chain" if result.get("just_promoted") else "err_chain_jump"
            await _db(db.update_game, game_id, new_board, turn, list(to_pos),
                           last_token_type=new_board[to_pos[0]][to_pos[1]],
                           error_msg=err_msg, err_recipient=user_id,
                           update_move_time=False)
            await callback.answer()
            asyncio.create_task(_refresh(err_msg, user_id))
            return

        next_turn = "black" if turn == "white" else "white"

        # Qalib yoxla
        winner_color = gl.check_win_condition(new_board)
        if winner_color:
            await _finish_game(game, game_id, new_board, winner_color, inline_id, callback)
            return

        # Bot gedişi — ardıcıl yeymə tam icra edilir
        if game_type == "bot" and next_turn == "black":
            await _db(db.update_game, game_id, new_board, "black", None,
                           error_msg=None, err_recipient=None,
                           update_move_time=True)
            try:
                await callback.answer()
            except Exception:
                pass
            asyncio.create_task(_bot_move_task_handler(game_id, new_board, inline_id))
            return

        await _db(db.update_game, game_id, new_board, next_turn, None,
                       error_msg=None, err_recipient=None,
                       update_move_time=True)

        if game_type == "bot":
            _start_timer(game_id, "white", p_white)
            # Bot tam sürətli oynayır, sleep yoxdur. _safe_edit limitləri daxili retry ilə həll edəcək.
        else:
            next_player = p_white if next_turn == "white" else p_black
            if next_player:
                _start_timer(game_id, next_turn, next_player)

        try:
            await callback.answer()
        except Exception:
            pass
        asyncio.create_task(_refresh())
        return

    # Yanlış klik
    await _db(db.update_game, game_id, board, turn, selected,
                   error_msg="err_invalid_move", err_recipient=user_id,
                   update_move_time=False)
    await callback.answer(t(lang, "err_invalid_move"), show_alert=True)
    asyncio.create_task(_refresh("err_invalid_move", user_id))


# ---------------------------------------------------------------------------
# _finish_game: ELO-lu oyun bitişi
# ---------------------------------------------------------------------------

async def _finish_game(game: dict, game_id: str, final_board: list,
                       winner_color: str, inline_id, callback):
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    game_type = game.get("game_type", "")

    winner_id = p_white if winner_color == "white" else (p_black or 0)
    loser_id  = p_black if winner_color == "white" else p_white

    winner_name = _display_name(winner_id)
    loser_name  = _display_name(loser_id)

    _timers.pop(game_id, None)
    db.delete_game(game_id)

    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and loser_id and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old_elo"], "w_new": w_args["new_elo"], "w_diff": w_args["delta"],
            "l_old": l_args["old_elo"], "l_new": l_args["new_elo"], "l_diff": l_args["delta"],
            "w_icon": w_icon, "l_icon": l_icon
        }
        wk = elo_data
        lk = elo_data
        msg_w, msg_l = "game_over_winner", "game_over_loser"
    else:
        # Bot oyunu
        if winner_id == 0:
            wk = {"winner": "Bot", "loser": loser_name}
            lk = {"winner": "Bot", "loser": loser_name}
            msg_w, msg_l = "bot_game_over_loser", "bot_game_over_loser"
        else:
            wk = {"winner": winner_name, "loser": "Bot"}
            lk = {"winner": winner_name, "loser": "Bot"}
            msg_w, msg_l = "bot_game_over_winner", "bot_game_over_winner" 

    await _send_game_over(game, game_id, winner_id, loser_id,
                          msg_w, msg_l, inline_id, wk, lk)
    await callback.answer()


# ---------------------------------------------------------------------------
# Bot süni zəka gedişi
# ---------------------------------------------------------------------------

def _execute_bot_turn(board: list) -> list:
    new_board = [row[:] for row in board]
    jumps = gl.get_all_mandatory_jumps(new_board, "black")
    if jumps:
        from_pos, to_pos, _ = random.choice(jumps)
        result = gl.validate_and_execute_move(new_board, from_pos, to_pos, "black")
        if result["status"] == "ok":
            new_board = result["board"]
            # Ardıcıl yeymə: eyni daşla davam et
            while result.get("chain_possible"):
                chain = gl.get_piece_jumps(new_board, to_pos, "black")
                if not chain:
                    break
                from_pos, to_pos, _ = random.choice(chain)
                result = gl.validate_and_execute_move(new_board, from_pos, to_pos, "black")
                if result["status"] != "ok":
                    break
                new_board = result["board"]
        return new_board
    moves = gl.get_all_possible_moves(new_board, "black")
    if moves:
        from_pos, to_pos = random.choice(moves)
        result = gl.validate_and_execute_move(new_board, from_pos, to_pos, "black")
        if result["status"] == "ok":
            new_board = result["board"]
    return new_board


# ---------------------------------------------------------------------------
# Təslim olmaq
# ---------------------------------------------------------------------------

@dp.callback_query(F.data.startswith("surrender_"))
async def cb_surrender(callback: types.CallbackQuery):
    game_id = callback.data[len("surrender_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return

    user_id   = callback.from_user.id
    lang      = _lang(user_id)
    p_white   = game["player_white"]
    p_black   = game["player_black"]
    game_type = game.get("game_type", "")

    if user_id not in [p_white, p_black]:
        await callback.answer(t(lang, "not_participant"), show_alert=True)
        return

    winner_id   = p_black if user_id == p_white else p_white
    loser_id    = user_id
    winner_name = _display_name(winner_id)
    loser_name  = _display_name(loser_id)
    inline_id   = callback.inline_message_id or game.get("inline_msg_id")

    _cancel_timer(game_id)
    db.delete_game(game_id)

    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old_elo"], "w_new": w_args["new_elo"], "w_diff": w_args["delta"],
            "l_old": l_args["old_elo"], "l_new": l_args["new_elo"], "l_diff": l_args["delta"],
            "w_icon": w_icon, "l_icon": l_icon
        }
        wk = elo_data
        lk = elo_data
        msg_w, msg_l = "surrender_winner", "surrender_loser"
    else:
        # Bot game surrender
        if loser_id == p_black or loser_id == 0:  # Bot surrendered
            wk = {"winner": winner_name, "loser": "Bot"}
            lk = {"winner": winner_name, "loser": "Bot"}
            msg_w, msg_l = "surrender_winner_bot", "surrender_winner_bot"
        else:  # User surrendered
            wk = {"winner": "Bot", "loser": loser_name}
            lk = {"winner": "Bot", "loser": loser_name}
            msg_w, msg_l = "surrender_loser_bot", "surrender_loser_bot" 

    await _send_game_over(game, game_id, winner_id, loser_id,
                          msg_w, msg_l, inline_id, wk, lk)
    await callback.answer()


# ---------------------------------------------------------------------------
# Heç-heçə TƏKLİFİ
# ---------------------------------------------------------------------------

@dp.callback_query(F.data.startswith("draw_offer_"))
async def cb_draw_offer(callback: types.CallbackQuery):
    game_id = callback.data[len("draw_offer_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return

    user_id = callback.from_user.id
    lang    = _lang(user_id)
    p_white = game["player_white"]
    p_black = game["player_black"]

    if user_id not in [p_white, p_black]:
        await callback.answer(t(lang, "not_participant"), show_alert=True)
        return

    # Bot ilə oyunda heç-heçə mümkün deyil
    if game.get("game_type") == "bot":
        await callback.answer(t(lang, "draw_bot_not_allowed"), show_alert=True)
        return

    if not p_black or p_black == 0:
        await callback.answer(t(lang, "no_opponent_yet"), show_alert=True)
        return
    if game.get("draw_offered_by") == user_id:
        await callback.answer(t(lang, "draw_already_offered"), show_alert=True)
        return

    db.update_game(game_id, game["board"], game["turn"], game["selected_cell"],
                   draw_offered_by=user_id, update_move_time=False)
    await callback.answer(t(lang, "draw_offer_sent"), show_alert=True)

    opponent_id = p_black if user_id == p_white else p_white
    lang_opp    = _lang(opponent_id)
    game_lang   = game.get("game_lang") or lang_opp
    builder     = InlineKeyboardBuilder()
    builder.button(text=t(lang_opp, "draw_accept_btn"), callback_data=f"draw_accept_{game_id}")
    builder.button(text=t(lang_opp, "draw_reject_btn"), callback_data=f"draw_reject_{game_id}")
    builder.adjust(2)

    inline_id = callback.inline_message_id or game.get("inline_msg_id")

    if inline_id:
        # Inline (qrup inline oyunu) — qrupa göndərilir (inline message-i redaktə et)
        try:
            await bot.edit_message_text(
                text=t(game_lang, "draw_offer_recv"),
                inline_message_id=inline_id,
                reply_markup=builder.as_markup(), parse_mode="HTML"
            )
        except Exception as e:
            logging.warning("Draw offer (inline): %s", e)
    elif game.get("shared_chat_id") and game.get("shared_msg_id"):
        # /saski friend (qrup mesajı) — QRUPA mesajı redaktə et (yeni mesaj göndərmə)
        try:
            await bot.edit_message_text(
                chat_id=game["shared_chat_id"],
                message_id=game["shared_msg_id"],
                text=t(game_lang, "draw_offer_recv"),
                reply_markup=builder.as_markup(), parse_mode="HTML"
            )
        except Exception as e:
            logging.warning("Draw offer (shared group): %s", e)
    else:
        # PvP şəxsi — rəqibin şəxsi chatına göndər
        try:
            await bot.send_message(
                opponent_id, text=t(lang_opp, "draw_offer_recv"),
                reply_markup=builder.as_markup(), parse_mode="HTML"
            )
        except Exception as e:
            logging.warning("Draw offer (private): %s", e)


# ---------------------------------------------------------------------------
# Heç-heçə QƏBULU
# ---------------------------------------------------------------------------

@dp.callback_query(F.data.startswith("draw_accept_"))
async def cb_draw_accept(callback: types.CallbackQuery):
    game_id = callback.data[len("draw_accept_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return

    user_id = callback.from_user.id
    p_white = game["player_white"]
    p_black = game["player_black"]

    # Yalnız oyunçular qəbul edə bilər
    if user_id not in [p_white, p_black]:
        offered_by = game.get("draw_offered_by")
        notif_lang = _lang(offered_by) if offered_by else (game.get("game_lang") or "az")
        await callback.answer(t(notif_lang, "not_participant"), show_alert=True)
        return

    # Teklif göndərən özü qəbul edə bilməz
    offered_by = game.get("draw_offered_by")
    if user_id == offered_by:
        await callback.answer(t(_lang(user_id), "draw_already_offered"), show_alert=True)
        return

    inline_id = callback.inline_message_id or game.get("inline_msg_id")
    _cancel_timer(game_id)
    db.delete_game(game_id)

    lang_w = _lang(p_white) if p_white else "az"
    lang_b = _lang(p_black) if p_black and p_black != 0 else lang_w

    if game["game_type"] in ("pvp", "friend", "friend_group", "friend_cmd") and p_white and p_black and p_black != 0:
        dw, dl = db.compute_elo_deltas(p_white, p_black, is_draw=True)
        db.update_stats(p_white, p_black, is_draw=True)
        w_args = _elo_args(p_white, dw)
        l_args = _elo_args(p_black, dl)
        elo_data = {
            "winner": _display_name(p_white), "loser": _display_name(p_black),
            "w_old": w_args["old_elo"], "w_new": w_args["new_elo"], "w_diff": w_args["delta"],
            "l_old": l_args["old_elo"], "l_new": l_args["new_elo"], "l_diff": l_args["delta"]
        }
        kw = elo_data
        kb = elo_data
    else:
        elo_data = {
            "winner": _display_name(p_white) if p_white else "Ağ", "loser": _display_name(p_black) if p_black else "Qara",
            "w_old": 1000, "w_new": 1000, "w_diff": "0",
            "l_old": 1000, "l_new": 1000, "l_diff": "0"
        }
        kw = elo_data
        kb = elo_data

    try:
        if inline_id:
            await bot.edit_message_text(
                text=t(lang_w, "draw_accepted_white", **kw),
                inline_message_id=inline_id,
                reply_markup=_board_markup(game["board"], game_id, lang_w, is_game_over=True),
                parse_mode="HTML"
            )
        elif game.get("shared_chat_id") and game.get("shared_msg_id"):
            game_lang = game.get("game_lang") or lang_w
            try:
                await bot.edit_message_text(
                    text=t(game_lang, "draw_accepted_white", **kw),
                    chat_id=game["shared_chat_id"],
                    message_id=game["shared_msg_id"],
                    reply_markup=_board_markup(game["board"], game_id, game_lang, is_game_over=True),
                    parse_mode="HTML"
                )
            except Exception:
                pass
            for uid, kargs in [(p_white, kw), (p_black, kb)]:
                if uid and uid != 0:
                    try:
                        await bot.send_message(
                            uid,
                            t(_lang(uid), "draw_accepted_white" if uid == p_white else "draw_accepted_black",
                              **kargs),
                            parse_mode="HTML"
                        )
                    except Exception:
                        pass
        else:
            if game.get("white_chat_id") and game.get("white_msg_id"):
                await bot.edit_message_text(
                    text=t(lang_w, "draw_accepted_white", **kw),
                    chat_id=game["white_chat_id"],
                    message_id=game["white_msg_id"], parse_mode="HTML"
                )
            if game.get("black_chat_id") and game.get("black_msg_id") and p_black and p_black != 0:
                try:
                    await bot.edit_message_text(
                        text=t(lang_b, "draw_accepted_black", **kb),
                        chat_id=game["black_chat_id"],
                        message_id=game["black_msg_id"], parse_mode="HTML"
                    )
                except Exception:
                    pass
    except Exception as e:
        logging.warning("draw_accept xetasi: %s", e)
    await callback.answer()


# ---------------------------------------------------------------------------
# Heç-heçə İMTİNASI
# ---------------------------------------------------------------------------

@dp.callback_query(F.data.startswith("draw_reject_"))
async def cb_draw_reject(callback: types.CallbackQuery):
    game_id = callback.data[len("draw_reject_"):]
    game    = db.get_game(game_id)
    if not game:
        await callback.answer()
        return

    user_id = callback.from_user.id
    lang    = _lang(user_id)
    p_white = game["player_white"]
    p_black = game["player_black"]

    # Yalnız oyunçular rədd edə bilər
    if user_id not in [p_white, p_black]:
        offered_by = game.get("draw_offered_by")
        notif_lang = _lang(offered_by) if offered_by else (game.get("game_lang") or "az")
        await callback.answer(t(notif_lang, "not_participant"), show_alert=True)
        return

    # Teklif göndərən özü rədd edə bilməz
    offered_by = game.get("draw_offered_by")
    if user_id == offered_by:
        await callback.answer(t(_lang(user_id), "draw_already_offered"), show_alert=True)
        return

    db.update_game(game_id, game["board"], game["turn"], game["selected_cell"],
                   draw_offered_by=0, update_move_time=False)

    inline_id = callback.inline_message_id or game.get("inline_msg_id")
    lang_w    = _lang(p_white) if p_white else "az"

    try:
        if inline_id:
            game_r = db.get_game(game_id)
            await bot.edit_message_text(
                text=_game_status_text(game_r, lang_w) if game_r else t(lang_w, "draw_rejected_notif"),
                inline_message_id=inline_id,
                reply_markup=_board_markup(game["board"], game_id, lang_w),
                parse_mode="HTML"
            )
        else:
            await _push_board_to_both(game_id)
    except Exception as e:
        logging.warning("draw_reject: %s", e)

    await callback.answer(t(lang, "draw_rejected_by_you"), show_alert=True)

    opponent_id = p_black if user_id == p_white else p_white
    if opponent_id and opponent_id != 0 and not inline_id:
        lang_opp = _lang(opponent_id)
        try:
            await bot.send_message(opponent_id, t(lang_opp, "draw_rejected_notif"),
                                   parse_mode="HTML")
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Boş xana
# ---------------------------------------------------------------------------

@dp.callback_query(F.data == "noop")
async def cb_noop(callback: types.CallbackQuery):
    await callback.answer()


# ---------------------------------------------------------------------------
# Başlatma
# ---------------------------------------------------------------------------

async def main():
    db.init_db()

    # ADDIM 1: Webhook-u sil (aktiv webhook varsa polling inline almır)
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Webhook silindi.")

    # ADDIM 2: Telegram server tərəfindəki allowed_updates abunəsini SIFIRLA.
    # Bu addım olmadan köhnə bot sessiyasından qalan keş "inline_query" tipini
    # exclude edə bilər — hətta start_polling-ə versək belə.
    _ALLOWED = ["message", "callback_query", "inline_query", "chosen_inline_result"]
    try:
        await bot.get_updates(timeout=0, allowed_updates=_ALLOWED)
        logging.info("Telegram allowed_updates abunəsi sıfırlandı: %s", _ALLOWED)
    except Exception as e:
        logging.warning("get_updates sıfırlama: %s", e)

    # ADDIM 3: Polling — eyni allowed_updates siyahısı ilə
    logging.info("Polling başlayır...")
    await dp.start_polling(bot, allowed_updates=_ALLOWED)


if __name__ == "__main__":
    asyncio.run(main())

@dp.callback_query(F.data == "ignore")
async def cb_ignore(callback: types.CallbackQuery):
    await callback.answer()
