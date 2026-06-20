import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

# Modify `elo_data = { ... }` blocks to include w_icon and l_icon
def repl_elo_data(match):
    old_elo_data = match.group(0)
    # Check if w_icon is already there
    if "w_icon" in old_elo_data:
        return old_elo_data
    # We can calculate w_icon and l_icon right before elo_data
    return """        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        elo_data = {
            "winner": winner_name, "loser": loser_name,
            "w_old": w_args["old_elo"], "w_new": w_args["new_elo"], "w_diff": w_args["delta"],
            "l_old": l_args["old_elo"], "l_new": l_args["new_elo"], "l_diff": l_args["delta"],
            "w_icon": w_icon, "l_icon": l_icon
        }"""

text = re.sub(r'\s*elo_data = \{\s*"winner": winner_name,\s*"loser": loser_name,\s*"w_old": w_args\["old_elo"\],\s*"w_new": w_args\["new_elo"\],\s*"w_diff": w_args\["delta"\],\s*"l_old": l_args\["old_elo"\],\s*"l_new": l_args\["new_elo"\],\s*"l_diff": l_args\["delta"\]\s*\}', repl_elo_data, text)

# Now, we also need to update the `else:` blocks where `wk = {"winner": winner_name}` is used, to include `w_icon` and `l_icon`.
def repl_wk_bot(match):
    # This matches wk = {"winner": winner_name} or similar
    # We will just inject w_icon and l_icon calculation before it, and add to dicts
    return """        w_icon = "⚪" if winner_id == p_white else "⚫"
        l_icon = "⚫" if winner_id == p_white else "⚪"
        wk = {"winner": winner_name, "loser": loser_name, "w_icon": w_icon, "l_icon": l_icon}
        lk = {"winner": winner_name, "loser": loser_name, "w_icon": w_icon, "l_icon": l_icon}"""

text = re.sub(r'        wk = \{"winner": winner_name, "loser": loser_name\}\n        lk = \{"winner": winner_name, "loser": loser_name\}', repl_wk_bot, text)

# For timeout_winner_bot
text = re.sub(r'        wk = \{"winner": winner_name\}\n        lk = \{"winner": winner_name\}', repl_wk_bot, text)
text = re.sub(r'        wk = \{"loser": loser_name\}\n        lk = \{"loser": loser_name\}', repl_wk_bot, text)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated w_icon and l_icon logic in main.py")
