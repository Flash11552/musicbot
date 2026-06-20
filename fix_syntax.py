import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "r", encoding="utf-8") as f:
    text = f.read()

# I will replace:
# ━━━━━━━━━━━━━━━━━━━━
#         "rating_menu": """
#
# with:
# ━━━━━━━━━━━━━━━━━━━━\"\"\",
#         "rating_menu": """
#
# But wait, let's see how many times it occurs without the closing quotes.

text = text.replace('━━━━━━━━━━━━━━━━━━━━\n        "rating_menu": """', '━━━━━━━━━━━━━━━━━━━━\"\"\",\n        "rating_menu": """')

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
