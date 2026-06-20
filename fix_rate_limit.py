import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    code = f.read()

safe_edit_new = """_last_edit_time = {}

async def _safe_edit(text: str, markup, chat_id=None, message_id=None, inline_message_id=None):
    \"\"\"Rate-limit-safe edit_message_text köməkçisi (versiya kontrolu və debouncer ilə).\"\"\"
    key = inline_message_id if inline_message_id else f"{chat_id}_{message_id}"
    version = time.time()
    _edit_versions[key] = version

    kwargs = dict(text=text, reply_markup=markup, parse_mode="HTML")
    if inline_message_id:
        kwargs["inline_message_id"] = inline_message_id
    else:
        kwargs["chat_id"] = chat_id
        kwargs["message_id"] = message_id

    is_group = bool(inline_message_id) or (chat_id and str(chat_id).startswith("-"))
    if is_group:
        now = time.time()
        last_time = _last_edit_time.get(key, 0)
        diff = now - last_time
        if diff < 1.3:  # limit to 1 edit per 1.3 seconds in groups
            await asyncio.sleep(1.3 - diff)
        
        if _edit_versions.get(key) != version:
            return  # Daha yeni bir edit tələbi var, bunu iptal et.

    try:
        if _edit_versions.get(key) != version:
            return
        await bot.edit_message_text(**kwargs)
        _last_edit_time[key] = time.time()
    except TelegramRetryAfter as e:
        _last_edit_time[key] = time.time() + e.retry_after
        await asyncio.sleep(e.retry_after + 0.1)
        if _edit_versions.get(key) == version:
            try:
                await bot.edit_message_text(**kwargs)
                _last_edit_time[key] = time.time()
            except Exception:
                pass
    except Exception as e:
        pass"""

code = re.sub(r'async def _safe_edit.*?pass\n\n\nasync def _push_board_to_both', safe_edit_new + '\n\n\nasync def _push_board_to_both', code, flags=re.DOTALL)

cb_cell_click_selection = """        await callback.answer(t(lang, "piece_selected") or "✅")
        is_group = (game_type in ("friend_group", "friend_cmd")) or bool(inline_id)
        if not is_group:
            asyncio.create_task(_refresh())
        return"""

code = re.sub(r'        await callback\.answer\(t\(lang, "piece_selected"\) or "✅"\)\n        asyncio\.create_task\(_refresh\(\)\)\n        return', cb_cell_click_selection, code)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Done")
