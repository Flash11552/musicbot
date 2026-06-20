import re
import json

# Import the existing locales
import sys
sys.path.insert(0, "/workspace/app-cej2tb5o4l4x/tasks/saski_bot")
from locales import LOCALES

def md_to_html(text):
    # Convert *...* to <b>...</b>
    text = re.sub(r'\*(.*?)\*', r'<b>\1</b>', text)
    # Convert _..._ to <i>...</i>
    text = re.sub(r'\_(.*?)\_', r'<i>\1</i>', text)
    # Replace /start with /saski in specific game over texts
    text = text.replace("Yeni oyun üçün /start", "Yeni oyun üçün /saski")
    text = text.replace("Use /start for a new game", "Use /saski for a new game")
    text = text.replace("Для новой игры /start", "Для новой игры /saski")
    text = text.replace("/start для новой", "/saski для новой")
    text = text.replace("Use /saski for a new game.", "Use /saski for a new game.")
    text = text.replace("👇 Yeni oyun üçün /start.", "👇 Yeni oyun üçün /saski.")
    
    # Remove the tip from help text
    lines = text.split('\n')
    lines = [l for l in lines if "Tip: /saski works the same" not in l and "Məsləhət: /saski" not in l and "Подсказка: /saski" not in l]
    return '\n'.join(lines)

# Apply to existing AZ, RU, EN
for lang in LOCALES:
    for key, val in LOCALES[lang].items():
        LOCALES[lang][key] = md_to_html(val)

# Load translated languages
with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/translated_locales.json", "r", encoding="utf-8") as f:
    translated = json.load(f)

for lang, tr_dict in translated.items():
    LOCALES[lang] = {}
    for key, val in tr_dict.items():
        LOCALES[lang][key] = md_to_html(val)

# Write to locales.py
with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write("# locales.py - 11 Dildə lokallaşdırma (HTML Format)\n")
    f.write("LOCALES = {\n")
    for lang, dic in LOCALES.items():
        f.write(f'    "{lang}": {{\n')
        for k, v in dic.items():
            # escape triple quotes and backslashes
            v_escaped = v.replace('\\', '\\\\').replace('"""', '\\"\\"\\"')
            f.write(f'        "{k}": """{v_escaped}""",\n')
        f.write("    },\n")
    f.write("}\n\n")
    f.write('def t(lang_code: str, key: str, **kwargs) -> str:\n')
    f.write('    if lang_code not in LOCALES:\n')
    f.write('        lang_code = "az"\n')
    f.write('    template = LOCALES[lang_code].get(key, LOCALES["az"].get(key, key))\n')
    f.write('    if kwargs:\n')
    f.write('        return template.format(**kwargs)\n')
    f.write('    return template\n')

print("locales.py generated successfully.")
