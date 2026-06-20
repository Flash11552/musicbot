import json

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace Sizin vaxtınız bitdi / У вас закончилось время / You ran out of time / etc with {loser} ran out of time
# Since they are essentially the same now, we can just replace the timeout_loser text with the exact timeout_winner text!
# Wait, for the timeout_loser, we can literally map it to the same string!
import re
text = re.sub(r'("timeout_loser":\s*""")([^"]*)"""', lambda m: m.group(0).replace(m.group(2), re.search(r'"timeout_winner":\s*"""([^"]*)"""', text[text.rfind('"', 0, m.start()):]).group(1) if re.search(r'"timeout_winner":\s*"""([^"]*)"""', text[text.rfind('"', 0, m.start()):]) else m.group(2)), text)

# 2. Replace 🟢 with {w_icon} and 🔴 with {l_icon} in timeout_winner and timeout_loser
text = text.replace("🟢 <b>{winner}:</b>", "{w_icon} <b>{winner}:</b>")
text = text.replace("🔴 <b>{loser}:</b>", "{l_icon} <b>{loser}:</b>")

# Also for game_over_winner, game_over_loser, surrender_winner, surrender_loser!
text = text.replace("🟢 <b>{winner}:</b>", "{w_icon} <b>{winner}:</b>")
text = text.replace("🔴 <b>{loser}:</b>", "{l_icon} <b>{loser}:</b>")

# 3. Profile text formatting: remove backticks around `{elo}`, `{total}`, `{wins}`, `{losses}`, `{draws}`
# e.g., 🏅 ELO Reytinq: `{elo}` -> 🏅 ELO Reytinq: {elo}
text = text.replace("`{elo}`", "{elo}")
text = text.replace("`{total}`", "{total}")
text = text.replace("`{wins}`", "{wins}")
text = text.replace("`{losses}`", "{losses}")
text = text.replace("`{draws}`", "{draws}")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Locales updated!")
