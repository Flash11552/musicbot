import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("""    # --- Boş xanaya və ya rəqibə klik — sadəcə xəbərdarlıq ---
    await callback.answer(t(lang, "err_invalid_move"))
    asyncio.create_task(_refresh("err_invalid_move", user_id))
    return""", """    # --- Boş xanaya və ya rəqibə klik — sadəcə xəbərdarlıq ---
    await callback.answer(t(lang, "err_invalid_move"))
    return""")

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Applied last refresh changes!")
