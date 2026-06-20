import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r'        if inline_id:\n.*?elif game\.get\("shared_chat_id"\)', text, re.DOTALL)
if match:
    old_code = match.group(0)
    new_code = """        if inline_id:
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
        elif game.get("shared_chat_id")"""
    text = text.replace(old_code, new_code)
    
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced inline PM logic!")
else:
    print("Match not found")
