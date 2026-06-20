import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()

new_safe_edit = """async def _safe_edit(text: str, markup, chat_id=None, message_id=None, inline_message_id=None):
    key = inline_message_id if inline_message_id else f"{chat_id}_{message_id}"
    version = time.time()
    _edit_versions[key] = version

    kwargs = dict(text=text, reply_markup=markup, parse_mode="HTML")
    if inline_message_id:
        kwargs["inline_message_id"] = inline_message_id
    else:
        kwargs["chat_id"] = chat_id
        kwargs["message_id"] = message_id

    while True:
        if _edit_versions.get(key) != version:
            return
        try:
            await bot.edit_message_text(**kwargs)
            return
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
        except Exception:
            return"""

text = re.sub(r'async def _safe_edit.*?_last_edit_time\[key\] = time\.time\(\) \+ e\.retry_after\n[^\n]*except Exception:\n[^\n]*pass', new_safe_edit, text, flags=re.DOTALL)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed safe edit")
