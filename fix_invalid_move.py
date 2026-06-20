import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

def repl_invalid_move(match):
    return """        if result["status"] == "error":
            # The board state hasn't actually changed in the DB.
            # Just show the popup and return to avoid rate limits!
            await callback.answer(t(lang, result["reason"]), show_alert=True)
            return"""

text = re.sub(r'        if result\["status"\] == "error":\n            board\[from_pos\[0\]\]\[from_pos\[1\]\] = gl\.SELECTED_MARK\n            await _db\(db\.update_game, game_id, board, turn, selected,\n                           last_token_type=real_token,\n                           error_msg=result\["reason"\], err_recipient=user_id,\n                           update_move_time=False\)\n            await callback\.answer\(t\(lang, result\["reason"\]\), show_alert=True\)\n            asyncio\.create_task\(_refresh\(result\["reason"\], user_id\)\)\n            return', repl_invalid_move, text)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Applied invalid move changes!")
