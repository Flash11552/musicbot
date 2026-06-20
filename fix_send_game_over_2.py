import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r'        else:\n            if game.get\("white_chat_id"\).*?pass', text, re.DOTALL)
if match:
    old_code = match.group(0)
    new_code = """        else:
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
                    pass"""
    text = text.replace(old_code, new_code)
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced!")
else:
    print("Match not found")
