import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (r'Saski Botuna Xoş Gəlmisiniz!', r'Şaşki Botuna Xoş Gəlmisiniz!'),
    (r'Saski Bot\'a hoş geldiniz!', r'Dama Bot\'a hoş geldiniz!'),
    (r'Saski Bot-ко кош келдиңиз!', r'Дойбу Ботуна кош келдиңиз!'),
    (r'Saski Bot-ga xush kelibsiz!', r'Shashka Botiga xush kelibsiz!'),
    (r'بوت الداما \(Saski\)!', r'بوت الداما!'),
    (r'Bot Saski!', r'Bot Checkers!'),
    (r'Saski Bot-qa', r'Дойбы Ботына'),
]

for old, new in replacements:
    text = re.sub(old, new, text)

# Check info strings as well
replacements_info = [
    (r'Saski Botuna Xoş Gəldiniz!', r'Şaşki Botuna Xoş Gəldiniz!'),
    (r'Saski Bot\'a Hoş Geldiniz!', r'Dama Bot\'a Hoş Geldiniz!'),
    (r'Saski Botко кош келиңиз!', r'Дойбу Ботуна кош келиңиз!'),
    (r'Saski Botga Xush Kelibsiz!', r'Shashka Botiga xush kelibsiz!'),
    (r'مرحبًا بك في بوت Saski!', r'مرحبًا بك في بوت الداما!'),
    (r'Selamat Datang di Bot Saski!', r'Selamat Datang di Bot Checkers!'),
]
for old, new in replacements_info:
    text = re.sub(old, new, text)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
