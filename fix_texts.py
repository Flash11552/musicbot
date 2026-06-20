import re

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove the Tip line
text = re.sub(r'\n+.*💡.*', '', text)

# 2. Replace Saski Bot in start_text for each language
replacements = {
    '<b>Saski Botuna Xoş Gəldiniz!</b>': '<b>Şaşki Botuna Xoş Gəldiniz!</b>',
    '<b>Добро пожаловать в Saski Bot!</b>': '<b>Добро пожаловать в Шашки Бот!</b>',
    '<b>Welcome to Saski Bot!</b>': '<b>Welcome to Checkers Bot!</b>',
    '<b>Saski Bot\'a Hoş Geldiniz!</b>': '<b>Dama Bot\'a Hoş Geldiniz!</b>',
    '<b>Saski Bot-қа қош келдіңіз!</b>': '<b>Дойбы Ботына қош келдіңіз!</b>',
    '<b>Saski Botко кош келиңиз!</b>': '<b>Дойбу Ботуна кош келиңиз!</b>',
    '<b>Saski Bot में आपका स्वागत है!</b>': '<b>चेकर्स बॉट में आपका स्वागत है!</b>',
    '<b>Saski Botga Xush Kelibsiz!</b>': '<b>Shashka Botga Xush Kelibsiz!</b>',
    '<b>مرحبًا بك في بوت Saski!</b>': '<b>مرحبًا بك في بوت الداما!</b>',
    '<b>Selamat Datang di Bot Saski!</b>': '<b>Selamat Datang di Bot Checkers!</b>',
    '<b>Sveiki atvykę į „Saski Bot“!</b>': '<b>Sveiki atvykę į Šaškių Botą!</b>',
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Done texts")
