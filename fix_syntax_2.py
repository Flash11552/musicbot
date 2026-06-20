import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("""# import uuid\n    game_id = f"friend_{user_id}_{str(uuid.uuid4())[:8]}" — sabit ID.""", """# game_id = f"friend_{user_id}_{uuid.uuid4()[:8]}" """)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed syntax")
