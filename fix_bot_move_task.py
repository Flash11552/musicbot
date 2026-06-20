import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

# I need to insert `async def _bot_move_task` before `cb_cell_click`.
bot_task_code = """
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

"""

# Insert `_bot_move_task_handler` before `cb_cell_click`
text = text.replace("@dp.callback_query(F.data.startswith(\"cell_\"))\nasync def cb_cell_click(callback: types.CallbackQuery):", bot_task_code + "\n@dp.callback_query(F.data.startswith(\"cell_\"))\nasync def cb_cell_click(callback: types.CallbackQuery):")

# Now replace the bot move logic inside cb_cell_click
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
            asyncio.create_task(_bot_move_task_handler(game_id, new_board, inline_id))
            return

        await _db(db.update_game, game_id, new_board, next_turn, None,
                       error_msg=None, err_recipient=None,
                       update_move_time=True)

        if game_type == "bot":
            _start_timer(game_id, "white", p_white)"""
    text = text.replace(old_code, new_code)
else:
    print("Match not found!")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated bot move logic to background task!")
