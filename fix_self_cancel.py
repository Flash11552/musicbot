import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("""        _cancel_timer(game_id)
        db.delete_game(game_id)

        if current_turn == "black":""", """        _timers.pop(game_id, None)
        db.delete_game(game_id)

        if current_turn == "black":""")

text = text.replace("""    winner_name = _display_name(winner_id)
    loser_name  = _display_name(loser_id)

    _cancel_timer(game_id)
    db.delete_game(game_id)

    if game_type in ("pvp", "friend", "friend_group", "friend_cmd")""", """    winner_name = _display_name(winner_id)
    loser_name  = _display_name(loser_id)

    _timers.pop(game_id, None)
    db.delete_game(game_id)

    if game_type in ("pvp", "friend", "friend_group", "friend_cmd")""")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Fixed self-cancel bug!")
