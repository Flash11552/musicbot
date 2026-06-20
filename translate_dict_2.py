import json
import urllib.request
import os
import sys

# Import the existing locales
sys.path.insert(0, "/workspace/app-cej2tb5o4l4x/tasks/saski_bot")
from locales import LOCALES

API_KEY = os.environ.get("INTEGRATIONS_API_KEY")

en_dict = LOCALES["en"]

prompt = f"""
I have a JSON dictionary of UI strings for a Checkers (Dama) Telegram bot in English.
Translate this dictionary into the following 8 languages, returning ONLY a valid JSON object containing the translations.
For each language code, provide the full translated dictionary.
The result must have this structure:
{{
  "tr": {{ ... }},
  "kk": {{ ... }},
  "ky": {{ ... }},
  "hi": {{ ... }},
  "uz": {{ ... }},
  "ar": {{ ... }},
  "id": {{ ... }},
  "lt": {{ ... }}
}}

Rules:
1. Translate contextually for a Telegram Bot interface playing Checkers.
2. The name of the game "Saski" should be translated contextually (e.g. "Dama" in Turkish, "Шашки" in Kyrgyz/Kazakh, "Checkers" in Hindi, etc. Or just "Saski (Dama)" etc.).
3. KEEP all placeholders exactly as they are: {{name}}, {{idx}}, {{val}}, {{sec}}, {{elo}}, {{total_games}}, {{wins}}, {{losses}}, {{draws}}, {{mode}}, {{white}}, {{black}}, {{winner}}, {{loser}}, {{w_old}}, {{w_new}}, {{w_diff}}, {{l_old}}, {{l_new}}, {{l_diff}}, {{lang}}, {{old}}, {{new}}, {{diff}}.
4. KEEP all emojis exactly as they are.
5. KEEP all HTML tags (<b>, <i>, etc.) exactly as they are.
6. The command /saski and /help should NOT be translated.
7. Return ONLY the raw JSON string. Do not use Markdown code blocks like ```json ... ```. Just the JSON object starting with {{ and ending with }}.

English Dictionary:
{json.dumps(en_dict, indent=2)}
"""

req_body = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    ]
}

req = urllib.request.Request(
    "https://app-cej2tb5o4l4x-api-VaOwP8E7dJqa.gateway.appmedo.com/v1beta/models/gemini-2.5-flash:streamGenerateContent?alt=sse",
    data=json.dumps(req_body).encode('utf-8'),
    headers={
        "Content-Type": "application/json",
        "X-Gateway-Authorization": f"Bearer {API_KEY}"
    },
    method="POST"
)

response_text = ""
try:
    with urllib.request.urlopen(req) as response:
        for line in response:
            line = line.decode('utf-8').strip()
            if line.startswith("data: "):
                data_str = line[6:]
                if data_str == "[DONE]":
                    break
                try:
                    data = json.loads(data_str)
                    if "candidates" in data and len(data["candidates"]) > 0:
                        part = data["candidates"][0]["content"]["parts"][0]
                        if "text" in part:
                            response_text += part["text"]
                except Exception as e:
                    pass
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

response_text = response_text.replace("```json", "").replace("```", "").strip()

try:
    translated_dict = json.loads(response_text)
    
    # Write to locales.py combining existing and new
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
        f.write("# locales.py - 11 Dildə lokallaşdırma (HTML Format)\n")
        f.write("LOCALES = {\n")
        
        # Write existing
        for lang in ['az', 'ru', 'en']:
            f.write(f'    "{lang}": {{\n')
            for k, v in LOCALES[lang].items():
                v_escaped = v.replace('\\', '\\\\').replace('"""', '\\"\\"\\"')
                f.write(f'        "{k}": """{v_escaped}""",\n')
            f.write("    },\n")
            
        # Write translated
        for lang, dic in translated_dict.items():
            f.write(f'    "{lang}": {{\n')
            for k, v in dic.items():
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

    print("Translation completed and locales.py updated.")
except Exception as e:
    print(f"Failed to parse JSON: {e}")
    with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/failed_translation.txt", "w", encoding="utf-8") as f:
        f.write(response_text)
