with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("`{total_games}`", "{total_games}")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Removed backticks from total_games")
