with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/main.py", "r", encoding="utf-8") as f:
    text = f.read()
import re
match = re.search(r'async def _safe_edit.*?return msg', text, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Not found")
