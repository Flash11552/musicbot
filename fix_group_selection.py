with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("""        is_group = (game_type in ("friend_group", "friend_cmd")) or bool(inline_id)\n        if not is_group:\n            asyncio.create_task(_refresh())\n        return""", """        asyncio.create_task(_refresh())\n        return""")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed group selection")
