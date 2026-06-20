import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

def repl_group_logic(match):
    return """    is_group = bool(
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
        text += "\\n\\n⚠️ *" + t(lang_display, error_code) + "*"
    return text"""

text = re.sub(r'    is_group = bool\(game\.get\("inline_msg_id"\) or game\.get\("shared_chat_id"\)\)\n    if is_group:\n        sec = 60\n    else:\n        sec = _remaining_sec\(game\)\n    turn = game\["turn"\]\n    if turn == "white":\n        turn_str = t\(lang_display, "turn_white", name=white_name, sec=sec\)\n    else:\n        tp = t\(lang_display, "bot_label"\) if game_type == "bot" else black_name\n        turn_str = t\(lang_display, "turn_black", name=tp, sec=sec\)\n\n    text = header \+ turn_str\n    if error_code and err_for_user is not None:\n        text \+= "\\n\\n⚠️ \*" \+ t\(lang_display, error_code\) \+ "\*"\n    return text', repl_group_logic, text)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Applied group bot fixes!")
