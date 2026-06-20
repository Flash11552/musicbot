import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace edit_message_text without reply_markup to include reply_markup in the else branch

old_str_w = """                await bot.edit_message_text(
                    text=txt_w,
                    chat_id=game["white_chat_id"],
                    message_id=game["white_msg_id"],
                    parse_mode="HTML"
                )"""

new_str_w = """                await bot.edit_message_text(
                    text=txt_w,
                    chat_id=game["white_chat_id"],
                    message_id=game["white_msg_id"],
                    reply_markup=_board_markup(game["board"], game_id, lang_w, is_game_over=True),
                    parse_mode="HTML"
                )"""

text = text.replace(old_str_w, new_str_w)

old_str_b = """                    await bot.edit_message_text(
                        text=txt_b,
                        chat_id=game["black_chat_id"],
                        message_id=game["black_msg_id"],
                        parse_mode="HTML"
                    )"""

new_str_b = """                    await bot.edit_message_text(
                        text=txt_b,
                        chat_id=game["black_chat_id"],
                        message_id=game["black_msg_id"],
                        reply_markup=_board_markup(game["board"], game_id, lang_b, is_game_over=True),
                        parse_mode="HTML"
                    )"""

text = text.replace(old_str_b, new_str_b)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed send_game_over")
