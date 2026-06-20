import asyncio
import time

_edit_queue = {}
_edit_task_running = {}

async def _process_queue(key):
    while key in _edit_queue:
        if not _edit_queue[key]:
            del _edit_queue[key]
            break
        
        # Get latest args
        kwargs = _edit_queue[key].pop()
        _edit_queue[key].clear() # drop older ones
        
        try:
            await kwargs["bot"].edit_message_text(**kwargs["kwargs"])
        except Exception as e:
            if "RetryAfter" in str(e):
                await asyncio.sleep(2)
        await asyncio.sleep(1.0) # Rate limit exactly 1 second

    _edit_task_running[key] = False

# Usage:
# _edit_queue[key].append({"bot": bot, "kwargs": kwargs})
# if not _edit_task_running.get(key):
#     _edit_task_running[key] = True
#     asyncio.create_task(_process_queue(key))
