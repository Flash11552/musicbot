import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace('"w_old": w_args["old"]', '"w_old": w_args["old_elo"]')
code = code.replace('"w_new": w_args["new"]', '"w_new": w_args["new_elo"]')
code = code.replace('"w_diff": w_args["diff"]', '"w_diff": w_args["delta"]')

code = code.replace('"l_old": l_args["old"]', '"l_old": l_args["old_elo"]')
code = code.replace('"l_new": l_args["new"]', '"l_new": l_args["new_elo"]')
code = code.replace('"l_diff": l_args["diff"]', '"l_diff": l_args["delta"]')

code = code.replace('"l_diff": str(dl).replace(\'-\',\'\')', '"l_diff": l_args["delta"]')

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(code)
print("Done")
