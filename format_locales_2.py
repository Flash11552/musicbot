import re

from locales import LOCALES

# First, modify LOCALES for 'az', 'ru', 'en'
az = LOCALES['az']
ru = LOCALES['ru']
en = LOCALES['en']

az["game_over_winner"] = "🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\n🎉 Təbriklər!\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"
az["game_over_loser"] = "🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\nSiz məğlub oldunuz.\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"
az["surrender_winner"] = "🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\n{loser} təslim oldu. 🎉 Təbriklər!\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"
az["surrender_loser"] = "🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\nSiz təslim oldunuz.\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"
az["timeout_winner"] = "⏱ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\n{loser} vaxtı bitdi.\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"
az["timeout_loser"] = "⏱ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>\nSizin vaxtınız bitdi.\n\n📈 <b>Nəticələr:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Yeni oyun üçün /saski"

az["game_over_draw"] = "🤝 <b>Oyun Bitdi — Heç-heçə!</b>\n\n📈 <b>Nəticələr:</b>\n⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})\n⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})\n\n👇 Yeni oyun üçün /saski"
az["draw_accepted_white"] = az["game_over_draw"]
az["draw_accepted_black"] = az["game_over_draw"]

az["bot_game_over_winner"] = "🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"
az["bot_game_over_loser"] = "🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"
az["surrender_winner_bot"] = "🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>\nBot təslim oldu.\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"
az["surrender_loser_bot"] = "🏳️ <b>Bot Oyunu Bitdi — Bot Qalib Gəldi!</b>\nSiz təslim oldunuz.\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"
az["timeout_winner_bot"] = "⏱ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>\nBotun vaxtı bitdi.\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"
az["timeout_loser_bot"] = "⏱ <b>Bot Oyunu Bitdi — Bot Qalib Gəldi!</b>\nSizin vaxtınız bitdi.\nℹ️ Bot oyunları statistikaya təsir etmir.\n\n👇 Yeni oyun üçün /saski"


ru["game_over_winner"] = "🏳️ <b>Игра Окончена — {winner} Победил!</b>\n🎉 Поздравляем!\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["game_over_loser"] = "🏳️ <b>Игра Окончена — {winner} Победил!</b>\nВы проиграли.\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["surrender_winner"] = "🏳️ <b>Игра Окончена — {winner} Победил!</b>\n{loser} сдался. 🎉 Поздравляем!\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["surrender_loser"] = "🏳️ <b>Игра Окончена — {winner} Победил!</b>\nВы сдались.\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["timeout_winner"] = "⏱ <b>Игра Окончена — {winner} Победил!</b>\nУ {loser} закончилось время.\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["timeout_loser"] = "⏱ <b>Игра Окончена — {winner} Победил!</b>\nУ вас закончилось время.\n\n📈 <b>Результаты:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Для новой игры /saski"
ru["game_over_draw"] = "🤝 <b>Игра Окончена — Ничья!</b>\n\n📈 <b>Результаты:</b>\n⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})\n⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})\n\n👇 Для новой игры /saski"
ru["draw_accepted_white"] = ru["game_over_draw"]
ru["draw_accepted_black"] = ru["game_over_draw"]

ru["bot_game_over_winner"] = "🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"
ru["bot_game_over_loser"] = "🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"
ru["surrender_winner_bot"] = "🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>\nБот сдался.\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"
ru["surrender_loser_bot"] = "🏳️ <b>Игра с ботом окончена — Бот Победил!</b>\nВы сдались.\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"
ru["timeout_winner_bot"] = "⏱ <b>Игра с ботом окончена — {winner} Победил!</b>\nУ бота закончилось время.\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"
ru["timeout_loser_bot"] = "⏱ <b>Игра с ботом окончена — Бот Победил!</b>\nУ вас закончилось время.\nℹ️ Игры с ботом не влияют на статистику.\n\n👇 Для новой игры /saski"

en["game_over_winner"] = "🏳️ <b>Game Over — {winner} Wins!</b>\n🎉 Congratulations!\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["game_over_loser"] = "🏳️ <b>Game Over — {winner} Wins!</b>\nYou lost.\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["surrender_winner"] = "🏳️ <b>Game Over — {winner} Wins!</b>\n{loser} surrendered. 🎉 Congratulations!\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["surrender_loser"] = "🏳️ <b>Game Over — {winner} Wins!</b>\nYou surrendered.\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["timeout_winner"] = "⏱ <b>Game Over — {winner} Wins!</b>\n{loser} ran out of time.\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["timeout_loser"] = "⏱ <b>Game Over — {winner} Wins!</b>\nYou ran out of time.\n\n📈 <b>Results:</b>\n🟢 <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})\n🔴 <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})\n\n👇 Use /saski for a new game"
en["game_over_draw"] = "🤝 <b>Game Over — Draw!</b>\n\n📈 <b>Results:</b>\n⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})\n⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})\n\n👇 Use /saski for a new game"
en["draw_accepted_white"] = en["game_over_draw"]
en["draw_accepted_black"] = en["game_over_draw"]

en["bot_game_over_winner"] = "🏳️ <b>Bot Game Over — {winner} Wins!</b>\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"
en["bot_game_over_loser"] = "🏳️ <b>Bot Game Over — {winner} Wins!</b>\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"
en["surrender_winner_bot"] = "🏳️ <b>Bot Game Over — {winner} Wins!</b>\nBot surrendered.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"
en["surrender_loser_bot"] = "🏳️ <b>Bot Game Over — Bot Wins!</b>\nYou surrendered.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"
en["timeout_winner_bot"] = "⏱ <b>Bot Game Over — {winner} Wins!</b>\nBot ran out of time.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"
en["timeout_loser_bot"] = "⏱ <b>Bot Game Over — Bot Wins!</b>\nYou ran out of time.\nℹ️ Bot games do not affect statistics.\n\n👇 Use /saski for a new game"

with open("/workspace/app-cej2tb5o4l4x/tasks/saski_bot/locales.py", "w", encoding="utf-8") as f:
    f.write("# locales.py - 11 Dildə lokallaşdırma (HTML Format)\n")
    f.write("LOCALES = {\n")
    for lang in ['az', 'ru', 'en']:
        f.write(f'    "{lang}": {{\n')
        for k, v in LOCALES[lang].items():
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

print("Modified locales.py successfully.")
