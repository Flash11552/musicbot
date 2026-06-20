import re

def rewrite_main():
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Update _board_markup to take is_game_over
    code = code.replace("def _board_markup(board: list, game_id: str, lang: str) -> types.InlineKeyboardMarkup:", "def _board_markup(board: list, game_id: str, lang: str, is_game_over: bool = False) -> types.InlineKeyboardMarkup:")
    
    code = code.replace("""        for c, cell in enumerate(row):
            text = " "
            if cell == "w":   text = "⛀"
            elif cell == "b": text = "⛂"
            elif cell == "W": text = "⛀"
            elif cell == "B": text = "⛂"
            builder.button(text=text, callback_data=f"c_{game_id}_{r}_{c}")""", """        for c, cell in enumerate(row):
            text = " "
            if cell == "w":   text = "⛀"
            elif cell == "b": text = "⛂"
            elif cell == "W": text = "⛀"
            elif cell == "B": text = "⛂"
            cb_data = f"c_{game_id}_{r}_{c}" if not is_game_over else "ignore"
            builder.button(text=text, callback_data=cb_data)""")

    code = code.replace("""    builder.button(text=t(lang, "btn_surrender"), callback_data=f"surrender_{game_id}")
    builder.button(text=t(lang, "btn_draw"),      callback_data=f"draw_offer_{game_id}")""", """    if not is_game_over:
        builder.button(text=t(lang, "btn_surrender"), callback_data=f"surrender_{game_id}")
        builder.button(text=t(lang, "btn_draw"),      callback_data=f"draw_offer_{game_id}")""")

    # 2. Add an ignore handler
    if "@dp.callback_query(F.data == \"ignore\")" not in code:
        code += "\n@dp.callback_query(F.data == \"ignore\")\nasync def cb_ignore(callback: types.CallbackQuery):\n    await callback.answer()\n"

    # 3. Update _send_game_over to pass is_game_over=True
    code = code.replace("""        if inline_id:
            # Inline mesaj: tək mesaj, qalib dilinə görə
            lang_show = game_lang or (_lang(winner_id) if winner_id else lang_w)
            await bot.edit_message_text(
                text=t(lang_show, msg_w_key, **wk),
                inline_message_id=inline_id,
                parse_mode="HTML"
            )""", """        if inline_id:
            # Inline mesaj: tək mesaj, qalib dilinə görə
            lang_show = game_lang or (_lang(winner_id) if winner_id else lang_w)
            await bot.edit_message_text(
                text=t(lang_show, msg_w_key, **wk),
                inline_message_id=inline_id,
                reply_markup=_board_markup(game["board"], game_id, lang_show, is_game_over=True),
                parse_mode="HTML"
            )""")
    
    code = code.replace("""            try:
                await bot.edit_message_text(
                    text=txt_w,
                    chat_id=game["shared_chat_id"],
                    message_id=game["shared_msg_id"],
                    parse_mode="HTML"
                )
            except Exception:
                pass""", """            try:
                await bot.edit_message_text(
                    text=txt_w,
                    chat_id=game["shared_chat_id"],
                    message_id=game["shared_msg_id"],
                    reply_markup=_board_markup(game["board"], game_id, lang_use, is_game_over=True),
                    parse_mode="HTML"
                )
            except Exception:
                pass""")

    # 4. _timer_check_game
    timer_block = """    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and loser_id \\
            and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old"], "w_new": w_args["new"], "w_diff": w_args["diff"],
            "l_old": l_args["old"], "l_new": l_args["new"], "l_diff": str(dl).replace('-','')
        }
        wk = elo_data
        lk = elo_data
        msg_w, msg_l = "timeout_winner", "timeout_loser"
    else:
        wk = {"winner": winner_name, "loser": loser_name}
        lk = {"winner": winner_name, "loser": loser_name}
        msg_w, msg_l = "timeout_winner_bot", "timeout_loser_bot" """
        
    code = re.sub(r'    if game_type in \("pvp", "friend", "friend_group", "friend_cmd"\) and winner_id and loser_id \\\n            and winner_id != 0 and loser_id != 0:\n        dw, dl = db.compute_elo_deltas.*?msg_w, msg_l = "timeout_winner_bot", "timeout_loser_bot"', timer_block, code, flags=re.DOTALL)

    # _finish_game
    finish_block = """    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and loser_id and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old"], "w_new": w_args["new"], "w_diff": w_args["diff"],
            "l_old": l_args["old"], "l_new": l_args["new"], "l_diff": str(dl).replace('-','')
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
            msg_w, msg_l = "bot_game_over_winner", "bot_game_over_winner" """

    code = re.sub(r'    if game_type in \("pvp", "friend", "friend_group", "friend_cmd"\) and winner_id and loser_id and winner_id != 0 and loser_id != 0:\n        dw, dl = db.compute_elo_deltas.*?msg_w, msg_l = "bot_game_over_winner", "bot_game_over_loser"', finish_block, code, flags=re.DOTALL)

    # cb_surrender
    surrender_block = """    if game_type in ("pvp", "friend", "friend_group", "friend_cmd") and winner_id and winner_id != 0 and loser_id != 0:
        dw, dl = db.compute_elo_deltas(winner_id, loser_id, is_draw=False)
        db.update_stats(winner_id, loser_id, is_draw=False)
        w_args = _elo_args(winner_id, dw)
        l_args = _elo_args(loser_id, dl)
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old"], "w_new": w_args["new"], "w_diff": w_args["diff"],
            "l_old": l_args["old"], "l_new": l_args["new"], "l_diff": str(dl).replace('-','')
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
            msg_w, msg_l = "surrender_loser_bot", "surrender_loser_bot" """

    code = re.sub(r'    if game_type in \("pvp", "friend", "friend_group", "friend_cmd"\) and winner_id and winner_id != 0 and loser_id != 0:\n        dw, dl = db.compute_elo_deltas.*?msg_w, msg_l = "surrender_winner_bot", "surrender_loser_bot"', surrender_block, code, flags=re.DOTALL)

    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
        f.write(code)

rewrite_main()
print("Done")
