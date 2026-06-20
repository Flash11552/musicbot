import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Modify `_game_status_text` to check if it's a group game and hardcode `sec`
def repl_status_text(match):
    old_code = match.group(0)
    new_code = """    is_group = bool(game.get("inline_msg_id") or game.get("shared_chat_id"))
    if is_group:
        sec = 60
    else:
        sec = _remaining_sec(game)
    turn = game["turn"]"""
    return new_code

text = re.sub(r'    sec  = _remaining_sec\(game\)\n    turn = game\["turn"\]', repl_status_text, text)

# 2. In `cb_cell_click`, DO NOT write "err_not_your_turn" to DB and DO NOT call _refresh.
def repl_not_turn(match):
    return """    if user_id != current_player:
        await callback.answer(t(lang, "err_not_your_turn"), show_alert=True)
        return"""

text = re.sub(r'    if user_id != current_player:\n        await _db\(db\.update_game, game_id, board, turn, selected,\n                       error_msg="err_not_your_turn", err_recipient=user_id,\n                       update_move_time=False\)\n        await callback\.answer\(t\(lang, "err_not_your_turn"\), show_alert=True\)\n        asyncio\.create_task\(_refresh\("err_not_your_turn", user_id\)\)\n        return', repl_not_turn, text)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Applied timer changes!")
