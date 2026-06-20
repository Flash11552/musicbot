with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('l_args = _elo_args(loser_id, dl)        w_icon = "⚪"', 'l_args = _elo_args(loser_id, dl)\n        w_icon = "⚪"')

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
