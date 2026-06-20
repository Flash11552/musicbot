import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r'        # Bot gedişi — ardıcıl yeymə tam icra edilir.*?_start_timer\(game_id, "white", p_white\)', text, re.DOTALL)
if match:
    old_code = match.group(0)
    new_code = """        # Bot gedişi — ardıcıl yeymə tam icra edilir
        if game_type == "bot" and next_turn == "black":
            await _db(db.update_game, game_id, new_board, "black", None,
                           error_msg=None, err_recipient=None,
                           update_move_time=True)
            try:
                await callback.answer()
            except Exception:
                pass
            await _refresh()
            await asyncio.sleep(0.4)
            new_board = _execute_bot_turn(new_board)
            after_bot = gl.check_win_condition(new_board)
            if after_bot:
                await _finish_game(game, game_id, new_board, after_bot, inline_id, callback)
                return
            next_turn = "white"

        await _db(db.update_game, game_id, new_board, next_turn, None,
                       error_msg=None, err_recipient=None,
                       update_move_time=True)

        if game_type == "bot":
            _start_timer(game_id, "white", p_white)"""
    text = text.replace(old_code, new_code)
    
    # Let's also wrap the bottom `await callback.answer()` in a try-except
    text = text.replace("await callback.answer()\n        asyncio.create_task(_refresh())", """try:\n            await callback.answer()\n        except Exception:\n            pass\n        asyncio.create_task(_refresh())""")
    
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced bot logic!")
else:
    print("Match not found")
