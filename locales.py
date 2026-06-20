# locales.py - 11 Dildə lokallaşdırma (HTML Format)
LOCALES = {
    "az": {
        "select_language": """🌍 <b>Dili seçin / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ Azərbaycan dili seçildi!""",
        "start_text": """⛀⛂ <b>Şaşki Botuna Xoş Gəlmisiniz!</b>

🎯 8×8 klassik dama oyunu — bot ilə, onlayn, ya da dost ilə!
🏆 ELO reytinq sistemi • ⚡ Real vaxtlı yeniləmə • ⏱ 60s/gediş

📖 Tam qaydalar üçün /help yazın.
👇 Aşağıdakı menyudan rejim seçin:""",
        "info": """⛀⛂ <b>Şaşki Botuna Xoş Gəlmisiniz!</b>

🎯 8×8 klassik dama oyunu — bot ilə, onlayn, ya da dost ilə!
🏆 ELO reytinq sistemi • ⚡ Real vaxtlı yeniləmə • ⏱ 60s/gediş

📖 Tam qaydalar üçün /help yazın.
👇 Aşağıdakı menyudan rejim seçin:""",
        "btn_profile": """👤 Mənim Səhifəm""",
        "btn_bot": """🤖 Bot ilə Oyna""",
        "btn_online": """🌐 Onlayn Oyna""",
        "btn_friend": """🤝 Dost ilə Oyna""",
        "btn_rating": """🏆 Reytinq""",
        "btn_other_bots": """📢 Kanalımız""",
        "btn_add_group": """➕ Qrupa Əlavə Et""",
        "btn_change_lang": """🌍 Dili Dəyiş""",
        "btn_back": """⬅️ Geri""",
        "btn_surrender": """🏳️ Təslim""",
        "btn_draw": """🤝 Heç-heçə""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Reytinq: {elo}

📊 Ümumi oyun: {total_games}
🏆 Qalibiyyət: {wins}
💔 Məğlubiyyət: {losses}
🤝 Heç-heçə: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Tam Bələdçi</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Əmrlər:</b>
• /start — Botu işə sal / menyuya qayıt
• /saski — Saski oyun menyusu (qrupda da işləyir)
• /my — Öz statistikanı gör
• /rating — ELO və qalibiyyət reytinqləri
• /language — Dili dəyiş

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Oyun Qaydaları:</b>
• ⚪ Ağ daşlar yuxarıya, ⚫ Qara daşlar aşağıya gedir
• Sadə daş: yalnız irəliyə hərəkət edir — amma GERİYƏ YEYƏ bilər
• Son sıraya çatdıqda → Dama (◻️/◼️) olur
• 👑 Dama: 4 istiqamətdə, istənilən məsafəyə gedir
• ⚡ Yeymə imkanı varsa MƏCBURAN yemək lazımdır
• 🔗 Bir gedişdə ardıcıl bir neçə daş yeyilə bilər
• 👑➡️⚡ Dama olan kimi yeyə biləcəyin daş varsa — MƏCBURAN DAVAM ET!
• Rəqibin bütün daşları yeyilərsə və ya gediş edə bilmirsə — SƏN QALİBSƏN!
• ⏱ Hər gediş üçün 60 saniyə — gecikənsə məğlub olursan!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Oyun Rejimləri:</b>
• 🤖 <b>Bot ilə</b> — Süni zəkaya qarşı məşq et (ELO təsir etmir)
• 🌐 <b>Onlayn</b> — Növbəyə gir, rəqib tap, oyna
• 🤝 <b>Dost ilə</b> — /saski yaz → Dost seç → Rəngi seç → Başla
  – Qrupa @SaskiGameBot yazaraq inline olaraq da göndərə bilərsən

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO Sistem:</b>
• Qalib: reytinq ↑   • Məğlub: reytinq ↓   • Heç-heçə: minimal dəyişir
• Bot oyunları ELO-ya təsir etmir — yalnız məşq üçündür

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Reytinq Menyusu</b>

Hansı siyahıya baxmaq istəyirsən?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Qalibiyyət""",
        "top_elo_title": """🏅 <b>TOP 20 — ƏN YÜKSƏK ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — ƏN ÇOX QALİB GƏLƏNLƏR</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} qalibiyyət
""",
        "turn_white": """Növbə: ⚪ <b>{name}</b>  ⏱ {sec}s""",
        "turn_black": """Növbə: ⚫ <b>{name}</b>  ⏱ {sec}s""",
        "board_header": """⛀⛂ <b>Saski</b> — {mode}

⚪ Ağ: <b>{white}</b>
⚫ Qara: <b>{black}</b>

""",
        "waiting_player": """gözlənilir…""",
        "bot_label": """Bot 🤖""",
        "saski_cmd_menu": """<b>Saski</b> — Rejim seçin:""",
        "saski_cmd_bot_btn": """🤖 Bot ilə Oyna""",
        "saski_cmd_frnd_btn": """🤝 Dost ilə Oyna""",
        "saski_btn_bot": """🤖 Bot ilə Oyna""",
        "saski_btn_friend": """🤝 Dost ilə Oyna""",
        "saski_menu_text": """⛀⛂ <b>Saski — Rejim Seçin</b>

🤖 <b>Bot ilə</b> — Məşq, ELO dəyişmir
🤝 <b>Dost ilə</b> — Rəng seç, birlikdə oyna""",
        "err_game_not_found": """⚠️ Oyun tapılmadı. Yenidən dəvət göndər.""",
        "draw_bot_not_allowed": """🤖 Bu oyun bot ilə idi — bot bərabərliyi qəbul edə bilməz.
Qalib ol ya məğlub ol! 💪""",
        "friend_pick_color_title": """🎮 <b>Dost ilə Oyun — Rəng Seçin</b>""",
        "friend_pick_color_text": """🎮 <b>Dost ilə Oyun</b>

Rənginizi seçin, sonra rəqibiniz qalan rəngi götürsün:

⚪ Ağ — Birinci gedişi edir
⚫ Qara — İkinci gedişi edir

⚪ Ağ: {white}
⚫ Qara: {black}""",
        "piece_selected": """✅ Daş seçildi, indi gedəcəyiniz xananı seçin""",
        "friend_lang_btn": """🌍 Oyun Dili Seçin""",
        "friend_game_over_shared": """🏁 <b>Oyun bitdi.</b>
{result}""",
        "mode_bot": """Bot rejimi""",
        "mode_pvp": """Onlayn""",
        "mode_friend": """Dost ilə""",
        "err_not_your_turn": """⛔ Bu sizin növbəniz deyil! Rəqibin gedişini gözləyin.""",
        "err_invalid_move": """❌ Bu gediş qanunsuz görünür. Başqa xana seçin.""",
        "err_must_jump": """⚠️ Məcburi yeymə var! Adi gediş edə bilməzsiniz — daşı atlamalısınız.""",
        "err_chain_jump": """🔗 Ardıcıl yeymə mümkündür! Bu gediş ilə daha daş yeyə bilərsiniz — davam edin.""",
        "err_king_must_jump": """👑 Damanız rəqib daşına yetirir! Yemək məcburidir — onu atlayın.""",
        "err_man_no_backward": """🚫 Sadə daş arxaya geda bilməz! Yalnız irəliyə gedə bilər (amma arxaya yeyə bilər).""",
        "err_no_piece_here": """🔍 Bu xanada sizin daşınız yoxdur. Öz daşınıza basın.""",
        "err_already_in_game": """🎮 Siz artıq aktiv oyundasınız! Onu bitirən kimi yeni oyun başlaya bilərsiniz.""",
        "err_king_promoted_chain": """👑⚡ Daş Damaya çevrildi! İndi yeyə biləcəyin bütün daşları VUR — məcburidir!""",
        "timeout_winner": """⏱ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>
{loser} vaxtı bitdi.

📈 <b>Nəticələr:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun üçün /saski""",
        "timeout_loser": """⏱ <b>Игра Окончена — {winner} Победил!</b>
У {loser} закончилось время.

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "draw_offer_sent": """🤝 Heç-heçə təklifi göndərildi. Rəqibinin cavabını gözlə…""",
        "draw_already_offered": """ℹ️ Siz artıq heç-heçə təklif etmisiniz. Cavabı gözləyin.""",
        "draw_offer_recv": """🤝 <b>Rəqibiniz heç-heçə təklif edir!</b>
Qəbul edirsinizmi?""",
        "draw_accept_btn": """✅ Razıyam""",
        "draw_reject_btn": """❌ Rədd edirəm""",
        "draw_accepted_white": """🤝 <b>Oyun Bitdi — Heç-heçə!</b>

📈 <b>Nəticələr:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun üçün /saski""",
        "draw_accepted_black": """🤝 <b>Oyun Bitdi — Heç-heçə!</b>

📈 <b>Nəticələr:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun üçün /saski""",
        "draw_rejected_by_you": """❌ Heç-heçəni rədd etdiniz. Oyun qaldığı yerdən davam edir.""",
        "draw_rejected_notif": """❌ Rəqibiniz heç-heçəni rədd etdi. Oyun davam edir!""",
        "no_opponent_yet": """⏳ Hələ rəqib yoxdur. Birinin qoşulmasını gözləyin.""",
        "not_participant": """🚫 Siz bu oyunun iştirakçısı deyilsiniz!""",
        "surrender_winner": """🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>
{loser} təslim oldu. 🎉 Təbriklər!

📈 <b>Nəticələr:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun üçün /saski""",
        "surrender_loser": """🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>
Siz təslim oldunuz.

📈 <b>Nəticələr:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun üçün /saski""",
        "game_over_hint": """

🔄 Yeni oyun üçün /saski""",
        "searching": """🔍 <b>Onlayn rəqib axtarılır…</b>

Lütfən gözləyin. Rəqib tapılanda oyun avtomatik başlayır.""",
        "cancel_search_btn": """❌ Axtarışı Dayandır""",
        "search_cancelled": """✅ Axtarış dayandırıldı.""",
        "already_searching": """ℹ️ Siz artıq axtarış növbəsindəsiniz.""",
        "match_found_white": """🎮 <b>Rəqib tapıldı! Oyun başlayır!</b>

Siz: ⚪ Ağ daşlar
Sizin addımınızla başlayır!

""",
        "match_found_black": """🎮 <b>Rəqib tapıldı! Oyun başlayır!</b>

Siz: ⚫ Qara daşlar
Rəqibinizin addımını gözləyin.

""",
        "bot_game_start": """🤖 <b>Bot ilə Saski Başladı!</b>

Siz: ⚪ Ağ daşlar
Bot: ⚫ Qara daşlar

Sizin addımınızla başlayır! Uğurlar! 🍀

""",
        "inline_title": """⚪⚫ Saski oyununu göndər!""",
        "inline_desc": """Bot ilə və ya dostla oyna — bu çata oyun masası göndərilir""",
        "inline_no_lang_btn": """👉 Bota keçin, dil seçin →""",
        "inline_no_lang_msg": """Əvvəl @SaskiGameBot-da /start yazın, dil seçin — sonra inline oyun göndərəcəksiniz!""",
        "group_color_select_msg": """🎮 <b>Saski — Qrupda Oyun</b>

Hər oyunçu öz rəngini seçsin:

⚪ Ağ — Birinci gedişi edir
⚫ Qara — İkinci gedişi edir

⚪ Ağ: {white}
⚫ Qara: {black}""",
        "group_select_lang_btn": """🌍 Dil Seç""",
        "group_lang_changed": """✅ Oyun dili dəyişdirildi.""",
        "group_waiting_color": """— gözlənilir —""",
        "friend_invite_title": """🎮 Saski — Dost ilə Oyna""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Saski — Dost ilə Oyun</b>

Oyunu başlatmaq üçün aşağıdan rənginizi seçin!
Birinci klikləyən seçdiyi rəngi alır, ikinci isə qalan rəngə düşür.

⚪ Ağ — Birinci gedişi edir
⚫ Qara — İkinci gedişi edir""",
        "friend_join_white_btn": """⚪ Ağ daşlarla oyna""",
        "friend_join_black_btn": """⚫ Qara daşlarla oyna""",
        "friend_color_taken": """⚠️ Bu rəng artıq seçilib! Digər rəngi seçin.""",
        "friend_game_starting": """🎮 Hər iki oyunçu qoşuldu! Oyun başlayır…""",
        "friend_you_white": """Siz ⚪ Ağ daşları seçdiniz!""",
        "friend_you_black": """Siz ⚫ Qara daşları seçdiniz!""",
        "friend_self_join": """⚠️ Özünüzlə oynamaq olmaz! Dostunuzu dəvət edin.""",
        "game_over_winner": """🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>
🎉 Təbriklər!

📈 <b>Nəticələr:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun üçün /saski""",
        "game_over_loser": """🏳️ <b>Oyun Bitdi — {winner} Qalib Gəldi!</b>
Siz məğlub oldunuz.

📈 <b>Nəticələr:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun üçün /saski""",
        "game_over_draw": """🤝 <b>Oyun Bitdi — Heç-heçə!</b>

📈 <b>Nəticələr:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun üçün /saski""",
        "bot_game_over_winner": """🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "bot_game_over_loser": """🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "surrender_winner_bot": """🏳️ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>
Bot təslim oldu.
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "surrender_loser_bot": """🏳️ <b>Bot Oyunu Bitdi — Bot Qalib Gəldi!</b>
Siz təslim oldunuz.
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "timeout_winner_bot": """⏱ <b>Bot Oyunu Bitdi — {winner} Qalib Gəldi!</b>
Botun vaxtı bitdi.
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "timeout_loser_bot": """⏱ <b>Bot Oyunu Bitdi — Bot Qalib Gəldi!</b>
Sizin vaxtınız bitdi.
ℹ️ Bot oyunları statistikaya təsir etmir.

👇 Yeni oyun üçün /saski""",
        "broadcast_no_perm": """🚫 Bu əmr yalnız adminlər üçündür.""",
        "broadcast_no_reply": """⚠️ Yayım etmək üçün bir mesajı cavab (reply) verin.""",
        "broadcast_done": """✅ Yayım tamamlandı: {ok} çatdırıldı, {fail} uğursuz.""",
        "group_game_start": """🎮 <b>Qrupda Saski Oyunu Başladı!</b>

Hamı oyna bilər — yalnız öz növbənizdə klik edin.""",
        "draw_is_your_offer": """ℹ️ Bu sizi öz teklifidir. Rəqibdən cavab gözləyin.""",
        "inline_bot_group_note": """🤖 Bot ilə oyun başladı! Yalnız siz daşları hərəkət edə bilərsiniz.""",
    },
    "ru": {
        "select_language": """🌍 <b>Dili seçin / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ Выбран русский язык!""",
        "start_text": """⛀⛂ <b>Добро пожаловать в Шашки Бот!</b>

🎯 Классические шашки 8×8 — против бота, онлайн или с другом!
🏆 ELO-рейтинг • ⚡ Ходы в реальном времени • ⏱ 60с на ход

📖 Полные правила: /help
👇 Выберите режим из меню:""",
        "info": """⛀⛂ <b>Добро пожаловать в Шашки Бот!</b>

🎯 Классические шашки 8×8 — против бота, онлайн или с другом!
🏆 ELO-рейтинг • ⚡ Ходы в реальном времени • ⏱ 60с на ход

📖 Полные правила: /help
👇 Выберите режим из меню:""",
        "btn_profile": """👤 Мой профиль""",
        "btn_bot": """🤖 Играть с ботом""",
        "btn_online": """🌐 Онлайн игра""",
        "btn_friend": """🤝 Играть с другом""",
        "btn_rating": """🏆 Рейтинг""",
        "btn_other_bots": """📢 Наш канал""",
        "btn_add_group": """➕ Добавить в группу""",
        "btn_change_lang": """🌍 Сменить язык""",
        "btn_back": """⬅️ Назад""",
        "btn_surrender": """🏳️ Сдаться""",
        "btn_draw": """🤝 Ничья""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Рейтинг: {elo}

📊 Всего игр: {total_games}
🏆 Победы: {wins}
💔 Поражения: {losses}
🤝 Ничьи: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Полное руководство</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Команды:</b>
• /start — Запустить бота / вернуться в меню
• /saski — Меню игры Saski (работает и в группах)
• /my — Своя статистика
• /rating — Таблицы рейтингов
• /language — Сменить язык

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Правила игры:</b>
• ⚪ Белые идут вверх, ⚫ чёрные — вниз
• Простая шашка: ходит только вперёд, но БЬЁТ НАЗАД
• Дошла до края → становится дамкой (◻️/◼️)
• 👑 Дамка: ходит во все 4 стороны на любое расстояние
• ⚡ При возможности взятия — взятие ОБЯЗАТЕЛЬНО
• 🔗 За один ход можно бить несколько шашек подряд
• 👑➡️⚡ Стала дамкой и есть взятие — ПРОДОЛЖАЙ БИТЬ ОБЯЗАТЕЛЬНО!
• Все шашки соперника съедены или он не может ходить — ТЫ ПОБЕДИЛ!
• ⏱ На ход 60 секунд — не успел = проиграл!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Режимы:</b>
• 🤖 <b>С ботом</b> — тренируйся против ИИ (ELO не меняется)
• 🌐 <b>Онлайн</b> — войди в очередь, найди соперника
• 🤝 <b>С другом</b> — /saski → Друг → выбери цвет → играй
  – Также через @SaskiGameBot в чате — отправь inline-приглашение

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO система:</b>
• Победа: рейтинг ↑   • Поражение: рейтинг ↓   • Ничья: минимально
• Игры с ботом на ELO не влияют — только для тренировки

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Меню рейтинга</b>

Какой список хотите посмотреть?""",
        "btn_top_elo": """🥇 ТОП 20 ELO""",
        "btn_top_wins": """⚔️ ТОП 20 Побед""",
        "top_elo_title": """🏅 <b>ТОП 20 — НАИВЫСШИЙ ELO</b>

""",
        "top_wins_title": """⚔️ <b>ТОП 20 — БОЛЬШЕ ВСЕГО ПОБЕД</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} побед
""",
        "turn_white": """Ход: ⚪ <b>{name}</b>  ⏱ {sec}с""",
        "turn_black": """Ход: ⚫ <b>{name}</b>  ⏱ {sec}с""",
        "board_header": """⛀⛂ <b>Шашки</b> — {mode}

⚪ Белые: <b>{white}</b>
⚫ Чёрные: <b>{black}</b>

""",
        "waiting_player": """ожидается…""",
        "bot_label": """Бот 🤖""",
        "saski_cmd_menu": """<b>Saski</b> — Выберите режим:""",
        "saski_cmd_bot_btn": """🤖 Играть с ботом""",
        "saski_cmd_frnd_btn": """🤝 Играть с другом""",
        "saski_btn_bot": """🤖 Играть с ботом""",
        "saski_btn_friend": """🤝 Играть с другом""",
        "saski_menu_text": """⛀⛂ <b>Saski — Выберите режим</b>

🤖 <b>С ботом</b> — Тренировка, ELO не меняется
🤝 <b>С другом</b> — Выбери цвет и играйте вместе""",
        "err_game_not_found": """⚠️ Игра не найдена. Отправь новое приглашение.""",
        "draw_bot_not_allowed": """🤖 Это игра с ботом — бот не принимает ничью.
Побеждай или проигрывай! 💪""",
        "friend_pick_color_title": """🎮 <b>Игра с другом — Выбор цвета</b>""",
        "friend_pick_color_text": """🎮 <b>Игра с другом</b>

Выберите свой цвет, соперник возьмёт оставшийся:

⚪ Белые — ходят первыми
⚫ Чёрные — ходят вторыми

⚪ Белые: {white}
⚫ Чёрные: {black}""",
        "piece_selected": """✅ Шашка выбрана, теперь выберите целевую клетку""",
        "friend_lang_btn": """🌍 Выбрать язык игры""",
        "friend_game_over_shared": """🏁 <b>Игра завершена.</b>
{result}""",
        "mode_bot": """Режим бота""",
        "mode_pvp": """Онлайн""",
        "mode_friend": """С другом""",
        "err_not_your_turn": """⛔ Сейчас не ваш ход! Дождитесь хода соперника.""",
        "err_invalid_move": """❌ Этот ход недопустим. Выберите другую клетку.""",
        "err_must_jump": """⚠️ Есть обязательное взятие! Нельзя просто ходить — нужно прыгнуть.""",
        "err_chain_jump": """🔗 Можно продолжить серию взятий! Вы можете ещё бить — продолжайте.""",
        "err_king_must_jump": """👑 Ваша дамка может срубить шашку соперника! Взятие обязательно.""",
        "err_man_no_backward": """🚫 Простая шашка не ходит назад! Только вперёд (но назад берёт).""",
        "err_no_piece_here": """🔍 На этой клетке нет вашей шашки. Нажмите на свою шашку.""",
        "err_already_in_game": """🎮 Вы уже в активной игре! Сначала завершите текущую партию.""",
        "err_king_promoted_chain": """👑⚡ Шашка стала дамкой! Теперь ОБЯЗАТЕЛЬНО бей все доступные шашки соперника!""",
        "timeout_winner": """⏱ <b>Игра Окончена — {winner} Победил!</b>
У {loser} закончилось время.

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "timeout_loser": """⏱ <b>Game Over — {winner} Wins!</b>
{loser} ran out of time.

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "draw_offer_sent": """🤝 Предложение ничьей отправлено. Ждём ответа…""",
        "draw_already_offered": """ℹ️ Вы уже предложили ничью. Ожидайте ответа.""",
        "draw_offer_recv": """🤝 <b>Соперник предлагает ничью!</b>
Вы согласны?""",
        "draw_accept_btn": """✅ Согласен""",
        "draw_reject_btn": """❌ Отклонить""",
        "draw_accepted_white": """🤝 <b>Игра Окончена — Ничья!</b>

📈 <b>Результаты:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Для новой игры /saski""",
        "draw_accepted_black": """🤝 <b>Игра Окончена — Ничья!</b>

📈 <b>Результаты:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Для новой игры /saski""",
        "draw_rejected_by_you": """❌ Вы отклонили ничью. Игра продолжается с того же места.""",
        "draw_rejected_notif": """❌ Соперник отклонил ничью. Игра продолжается!""",
        "no_opponent_yet": """⏳ Пока нет соперника. Ждите, пока кто-то присоединится.""",
        "not_participant": """🚫 Вы не являетесь участником этой игры!""",
        "surrender_winner": """🏳️ <b>Игра Окончена — {winner} Победил!</b>
{loser} сдался. 🎉 Поздравляем!

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "surrender_loser": """🏳️ <b>Игра Окончена — {winner} Победил!</b>
Вы сдались.

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "game_over_hint": """

🔄 Новая игра: /start""",
        "searching": """🔍 <b>Поиск онлайн соперника…</b>

Пожалуйста, подождите.""",
        "cancel_search_btn": """❌ Остановить поиск""",
        "search_cancelled": """✅ Поиск остановлен.""",
        "already_searching": """ℹ️ Вы уже в очереди поиска.""",
        "match_found_white": """🎮 <b>Соперник найден! Игра начинается!</b>

Вы: ⚪ Белые
Ваш ход первый!

""",
        "match_found_black": """🎮 <b>Соперник найден! Игра начинается!</b>

Вы: ⚫ Чёрные
Ожидайте хода соперника.

""",
        "bot_game_start": """🤖 <b>Игра с ботом началась!</b>

Вы: ⚪ Белые
Бот: ⚫ Чёрные

Ваш ход первый! Удачи! 🍀

""",
        "inline_title": """⚪⚫ Отправить игру в шашки!""",
        "inline_desc": """С ботом или с другом — доска отправится в этот чат""",
        "inline_no_lang_btn": """👉 Перейти к боту, выбрать язык →""",
        "inline_no_lang_msg": """Сначала напишите /start в @SaskiGameBot и выберите язык — потом отправляйте inline-игру!""",
        "group_color_select_msg": """🎮 <b>Saski — Игра в группе</b>

Каждый игрок выбирает свой цвет:

⚪ Белые — ходят первыми
⚫ Чёрные — ходят вторыми

⚪ Белые: {white}
⚫ Чёрные: {black}""",
        "group_select_lang_btn": """🌍 Выбрать язык""",
        "group_lang_changed": """✅ Язык игры изменён.""",
        "group_waiting_color": """— ожидается —""",
        "friend_invite_title": """🎮 Saski — Играть с другом""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Saski — Игра с другом</b>

Выберите свой цвет ниже!
Первый нажавший получает выбранный цвет, второй — оставшийся.

⚪ Белые — ходят первыми
⚫ Чёрные — ходят вторыми""",
        "friend_join_white_btn": """⚪ Играть белыми""",
        "friend_join_black_btn": """⚫ Играть чёрными""",
        "friend_color_taken": """⚠️ Этот цвет уже занят! Выберите другой.""",
        "friend_game_starting": """🎮 Оба игрока подключились! Игра начинается…""",
        "friend_you_white": """Вы выбрали ⚪ Белые!""",
        "friend_you_black": """Вы выбрали ⚫ Чёрные!""",
        "friend_self_join": """⚠️ Нельзя играть с самим собой! Пригласите друга.""",
        "game_over_winner": """🏳️ <b>Игра Окончена — {winner} Победил!</b>
🎉 Поздравляем!

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "game_over_loser": """🏳️ <b>Игра Окончена — {winner} Победил!</b>
Вы проиграли.

📈 <b>Результаты:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Для новой игры /saski""",
        "game_over_draw": """🤝 <b>Игра Окончена — Ничья!</b>

📈 <b>Результаты:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Для новой игры /saski""",
        "bot_game_over_winner": """🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "bot_game_over_loser": """🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "surrender_winner_bot": """🏳️ <b>Игра с ботом окончена — {winner} Победил!</b>
Бот сдался.
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "surrender_loser_bot": """🏳️ <b>Игра с ботом окончена — Бот Победил!</b>
Вы сдались.
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "timeout_winner_bot": """⏱ <b>Игра с ботом окончена — {winner} Победил!</b>
У бота закончилось время.
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "timeout_loser_bot": """⏱ <b>Игра с ботом окончена — Бот Победил!</b>
У вас закончилось время.
ℹ️ Игры с ботом не влияют на статистику.

👇 Для новой игры /saski""",
        "broadcast_no_perm": """🚫 Эта команда только для администраторов.""",
        "broadcast_no_reply": """⚠️ Чтобы сделать рассылку, ответьте (reply) на сообщение.""",
        "broadcast_done": """✅ Рассылка завершена: {ok} доставлено, {fail} ошибок.""",
        "group_game_start": """🎮 <b>Игра в Saski началась в группе!</b>

Можно нажимать только в свой ход.""",
        "draw_is_your_offer": """ℹ️ Это ваше предложение ничьей. Ожидайте ответа соперника.""",
        "inline_bot_group_note": """🤖 Игра с ботом началась! Только вы можете делать ходы.""",
    },
    "en": {
        "select_language": """🌍 <b>Dili seçin / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ English selected!""",
        "start_text": """⛀⛂ <b>Welcome to Checkers Bot!</b>

🎯 Classic 8×8 checkers — vs bot, online, or with a friend!
🏆 ELO rating system • ⚡ Real-time moves • ⏱ 60s per move

📖 Full rules: /help
👇 Pick a mode from the menu:""",
        "info": """⛀⛂ <b>Welcome to Checkers Bot!</b>

🎯 Classic 8×8 checkers — vs bot, online, or with a friend!
🏆 ELO rating system • ⚡ Real-time moves • ⏱ 60s per move

📖 Full rules: /help
👇 Pick a mode from the menu:""",
        "btn_profile": """👤 My Profile""",
        "btn_bot": """🤖 Play vs Bot""",
        "btn_online": """🌐 Play Online""",
        "btn_friend": """🤝 Play with Friend""",
        "btn_rating": """🏆 Leaderboard""",
        "btn_other_bots": """📢 Our Channel""",
        "btn_add_group": """➕ Add to Group""",
        "btn_change_lang": """🌍 Change Language""",
        "btn_back": """⬅️ Back""",
        "btn_surrender": """🏳️ Surrender""",
        "btn_draw": """🤝 Draw""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Rating: {elo}

📊 Total games: {total_games}
🏆 Wins: {wins}
💔 Losses: {losses}
🤝 Draws: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Full Guide</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Commands:</b>
• /start — Start the bot / back to menu
• /saski — Saski game menu (works in groups too)
• /my — Your stats
• /rating — ELO & wins leaderboards
• /language — Change language

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Rules:</b>
• ⚪ White moves up the board, ⚫ Black moves down
• Regular piece: moves forward only — but CAN CAPTURE BACKWARD
• Reaches the far row → becomes a king (◻️/◼️)
• 👑 King: moves in all 4 directions, any distance
• ⚡ Captures are MANDATORY when available
• 🔗 Chain captures: keep jumping in a single turn
• 👑➡️⚡ Just became a king and can capture? MUST continue immediately!
• All opponent pieces captured or blocked — YOU WIN!
• ⏱ 60 seconds per move — run out = you lose!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Modes:</b>
• 🤖 <b>vs Bot</b> — Practice against AI (ELO unaffected)
• 🌐 <b>Online</b> — Join the queue, find an opponent
• 🤝 <b>Friend</b> — /saski → Friend → pick colour → play
  – Or send an inline invite via @SaskiGameBot in any chat

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO system:</b>
• Win: rating ↑   • Loss: rating ↓   • Draw: minimal change
• Bot games don't affect ELO — practice only

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Leaderboard Menu</b>

Which list would you like to view?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Wins""",
        "top_elo_title": """🏅 <b>TOP 20 — HIGHEST ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — MOST WINS</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} wins
""",
        "turn_white": """Turn: ⚪ <b>{name}</b>  ⏱ {sec}s""",
        "turn_black": """Turn: ⚫ <b>{name}</b>  ⏱ {sec}s""",
        "board_header": """⛀⛂ <b>Checkers</b> — {mode}

⚪ White: <b>{white}</b>
⚫ Black: <b>{black}</b>

""",
        "waiting_player": """waiting…""",
        "bot_label": """Bot 🤖""",
        "saski_cmd_menu": """<b>Saski</b> — Choose mode:""",
        "saski_cmd_bot_btn": """🤖 Play vs Bot""",
        "saski_cmd_frnd_btn": """🤝 Play with Friend""",
        "saski_btn_bot": """🤖 Play vs Bot""",
        "saski_btn_friend": """🤝 Play with Friend""",
        "saski_menu_text": """⛀⛂ <b>Saski — Choose Mode</b>

🤖 <b>vs Bot</b> — Practice, ELO unaffected
🤝 <b>Friend</b> — Pick a colour and play together""",
        "err_game_not_found": """⚠️ Game not found. Please send a new invite.""",
        "draw_bot_not_allowed": """🤖 This is a bot game — the bot can't accept a draw.
Win or lose! 💪""",
        "friend_pick_color_title": """🎮 <b>Friend Game — Pick Colour</b>""",
        "friend_pick_color_text": """🎮 <b>Friend Game</b>

Pick your colour; your opponent takes the other:

⚪ White — moves first
⚫ Black — moves second

⚪ White: {white}
⚫ Black: {black}""",
        "piece_selected": """✅ Piece selected, now pick the destination square""",
        "friend_lang_btn": """🌍 Select Game Language""",
        "friend_game_over_shared": """🏁 <b>Game over.</b>
{result}""",
        "mode_bot": """vs Bot""",
        "mode_pvp": """Online""",
        "mode_friend": """vs Friend""",
        "err_not_your_turn": """⛔ It's not your turn! Wait for your opponent.""",
        "err_invalid_move": """❌ That move is not allowed. Pick another square.""",
        "err_must_jump": """⚠️ A capture is available! You must jump — normal moves are not allowed.""",
        "err_chain_jump": """🔗 Chain capture possible! You can keep jumping — continue the sequence.""",
        "err_king_must_jump": """👑 Your king can capture an opponent piece! Capturing is mandatory.""",
        "err_man_no_backward": """🚫 Regular pieces can't move backward! Forward only (but can capture backward).""",
        "err_no_piece_here": """🔍 There's no piece of yours here. Tap on your own piece.""",
        "err_already_in_game": """🎮 You're already in an active game! Finish it before starting a new one.""",
        "err_king_promoted_chain": """👑⚡ Piece promoted to king! Now you MUST capture all available opponent pieces!""",
        "timeout_winner": """⏱ <b>Game Over — {winner} Wins!</b>
{loser} ran out of time.

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "timeout_loser": """⏲️ <b>Oyun Bitti — Kazanan: {winner}!</b>
{loser} süreyi bitirdi.

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "draw_offer_sent": """🤝 Draw offer sent. Waiting for response…""",
        "draw_already_offered": """ℹ️ You already offered a draw. Waiting for opponent's response.""",
        "draw_offer_recv": """🤝 <b>Your opponent offers a draw!</b>
Do you accept?""",
        "draw_accept_btn": """✅ Accept""",
        "draw_reject_btn": """❌ Decline""",
        "draw_accepted_white": """🤝 <b>Game Over — Draw!</b>

📈 <b>Results:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Use /saski for a new game""",
        "draw_accepted_black": """🤝 <b>Game Over — Draw!</b>

📈 <b>Results:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Use /saski for a new game""",
        "draw_rejected_by_you": """❌ You declined the draw. Game continues from where it left off.""",
        "draw_rejected_notif": """❌ Your opponent declined the draw. Game continues!""",
        "no_opponent_yet": """⏳ No opponent yet. Wait for someone to join.""",
        "not_participant": """🚫 You are not a participant in this game!""",
        "surrender_winner": """🏳️ <b>Game Over — {winner} Wins!</b>
{loser} surrendered. 🎉 Congratulations!

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "surrender_loser": """🏳️ <b>Game Over — {winner} Wins!</b>
You surrendered.

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "game_over_hint": """

🔄 New game: /start""",
        "searching": """🔍 <b>Searching for an online opponent…</b>

Please wait.""",
        "cancel_search_btn": """❌ Cancel Search""",
        "search_cancelled": """✅ Search cancelled.""",
        "already_searching": """ℹ️ You are already in the search queue.""",
        "match_found_white": """🎮 <b>Opponent found! Game starting!</b>

You: ⚪ White
Your move is first!

""",
        "match_found_black": """🎮 <b>Opponent found! Game starting!</b>

You: ⚫ Black
Wait for opponent's move.

""",
        "bot_game_start": """🤖 <b>Game vs Bot started!</b>

You: ⚪ White
Bot: ⚫ Black

Your move is first! Good luck! 🍀

""",
        "inline_title": """⚪⚫ Send a Checkers game!""",
        "inline_desc": """vs Bot or with a Friend — the board lands right in this chat""",
        "inline_no_lang_btn": """👉 Go to bot, choose language →""",
        "inline_no_lang_msg": """First send /start to @SaskiGameBot and pick a language — then you can send inline games!""",
        "group_color_select_msg": """🎮 <b>Saski — Group Game</b>

Each player picks their colour:

⚪ White — moves first
⚫ Black — moves second

⚪ White: {white}
⚫ Black: {black}""",
        "group_select_lang_btn": """🌍 Select Language""",
        "group_lang_changed": """✅ Game language changed.""",
        "group_waiting_color": """— waiting —""",
        "friend_invite_title": """🎮 Saski — Play with Friend""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Saski — Friend Game</b>

Pick your colour below!
First to click gets that colour, second gets the other.

⚪ White — moves first
⚫ Black — moves second""",
        "friend_join_white_btn": """⚪ Play as White""",
        "friend_join_black_btn": """⚫ Play as Black""",
        "friend_color_taken": """⚠️ That colour is taken! Choose the other one.""",
        "friend_game_starting": """🎮 Both players joined! Game is starting…""",
        "friend_you_white": """You chose ⚪ White!""",
        "friend_you_black": """You chose ⚫ Black!""",
        "friend_self_join": """⚠️ You can't play against yourself! Invite a friend.""",
        "game_over_winner": """🏳️ <b>Game Over — {winner} Wins!</b>
🎉 Congratulations!

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "game_over_loser": """🏳️ <b>Game Over — {winner} Wins!</b>
You lost.

📈 <b>Results:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Use /saski for a new game""",
        "game_over_draw": """🤝 <b>Game Over — Draw!</b>

📈 <b>Results:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Use /saski for a new game""",
        "bot_game_over_winner": """🏳️ <b>Bot Game Over — {winner} Wins!</b>
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "bot_game_over_loser": """🏳️ <b>Bot Game Over — {winner} Wins!</b>
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "surrender_winner_bot": """🏳️ <b>Bot Game Over — {winner} Wins!</b>
Bot surrendered.
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "surrender_loser_bot": """🏳️ <b>Bot Game Over — Bot Wins!</b>
You surrendered.
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "timeout_winner_bot": """⏱ <b>Bot Game Over — {winner} Wins!</b>
Bot ran out of time.
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "timeout_loser_bot": """⏱ <b>Bot Game Over — Bot Wins!</b>
You ran out of time.
ℹ️ Bot games do not affect statistics.

👇 Use /saski for a new game""",
        "broadcast_no_perm": """🚫 This command is for admins only.""",
        "broadcast_no_reply": """⚠️ Reply to a message to broadcast it.""",
        "broadcast_done": """✅ Broadcast done: {ok} delivered, {fail} failed.""",
        "group_game_start": """🎮 <b>Saski game started in this group!</b>

Click only on your turn.""",
        "draw_is_your_offer": """ℹ️ This is your own draw offer. Wait for your opponent's response.""",
        "inline_bot_group_note": """🤖 Bot game started! Only you can make moves.""",
    },
    "tr": {
        "select_language": """🌍 <b>Dili seçin / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ İngilizce seçildi!""",
        "start_text": """⛀⛂ <b>Dama Bot\'a hoş geldiniz!</b>

🎯 Klasik 8x8 dama — botla, çevrimiçi veya arkadaşınızla!
🏆 ELO derecelendirme sistemi • ⚡ Gerçek zamanlı hamleler • ⏲️ Hamle başına 60sn

📖 Tüm kurallar: /help
👇 Menüden bir mod seçin:""",
        "info": """⛀⛂ <b>Dama Bot\'a hoş geldiniz!</b>

🎯 Klasik 8x8 dama — botla, çevrimiçi veya arkadaşınızla!
🏆 ELO derecelendirme sistemi • ⚡ Gerçek zamanlı hamleler • ⏲️ Hamle başına 60sn

📖 Tüm kurallar: /help
👇 Menüden bir mod seçin:""",
        "btn_profile": """👤 Profilim""",
        "btn_bot": """🤖 Botla Oyna""",
        "btn_online": """🌐 Çevrimiçi Oyna""",
        "btn_friend": """🤝 Arkadaşla Oyna""",
        "btn_rating": """🏆 Skor Tablosu""",
        "btn_other_bots": """📢 Kanalımız""",
        "btn_add_group": """➕ Gruba Ekle""",
        "btn_change_lang": """🌍 Dili Değiştir""",
        "btn_back": """🔙 Geri""",
        "btn_surrender": """🏳️ Teslim Ol""",
        "btn_draw": """🤝 Beraberlik""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Puanı: {elo}

📊 Toplam oyun: {total_games}
🏆 Galibiyet: {wins}
💔 Mağlubiyet: {losses}
🤝 Beraberlik: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Tam Kılavuz</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Komutlar:</b>
• /start — Botu başlat / menüye dön
• /saski — Saski oyun menüsü (gruplarda da çalışır)
• /my — İstatistikleriniz
• /rating — ELO & galibiyet sıralaması
• /language — Dil değiştirme

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Kurallar:</b>
• ⚪ Beyaz yukarı, ⚫ Siyah aşağı doğru ilerler
• Normal taş: sadece ileri gider — ancak GERİYE DOĞRU YİYEBİLİR
• Son sıraya ulaşan → dama olur (◻️/◼️)
• 👑 Dama: 4 yöne de, her mesafeye hareket eder
• ⚡ Yer varsa yeme ZORUNLUDUR
• 🔗 Zincirleme yeme: tek hamlede zıplamaya devam edin
• 👑➡⚡ Yeni dama oldu ve yeme imkanı var mı? Hemen devam etmelisiniz!
• Tüm rakip taşlar alındı veya kilitlendi → KAZANDINIZ!
• ⏲️ Her hamle için 60 saniye — süre biterse kaybedersiniz!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Modlar:</b>
• 🤖 <b>Botla</b> — Yapay zekaya karşı pratik (ELO değişmez)
• 🌐 <b>Çevrimiçi</b> — Sıraya gir, rakip bul
• 🤝 <b>Arkadaş</b> — /saski → Arkadaş → renk seç → oyna
  – Veya herhangi bir sohbette @SaskiGameBot üzerinden davet gönderin

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO sistemi:</b>
• Galibiyet: puan ↑   • Mağlubiyet: puan ↓   • Beraberlik: minimum değişim
• Bot oyunları ELO'yu etkilemez — sadece pratik içindir

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Skor Tablosu Menüsü</b>

Hangi listeyi görmek istersiniz?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Galibiyet""",
        "top_elo_title": """🏅 <b>TOP 20 — EN YÜKSEK ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — EN ÇOK GALİBİYET</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} galibiyet
""",
        "turn_white": """Sıra: ⚪ <b>{name}</b>  ⏲️ {sec}sn""",
        "turn_black": """Sıra: ⚫ <b>{name}</b>  ⏲️ {sec}sn""",
        "board_header": """⛀⛂ <b>Dama</b> — {mode}

⚪ Beyaz: <b>{white}</b>
⚫ Siyah: <b>{black}</b>

""",
        "waiting_player": """bekleniyor…""",
        "bot_label": """Bot 🤖""",
        "saski_cmd_menu": """<b>Saski</b> — Mod seçin:""",
        "saski_cmd_bot_btn": """🤖 Botla Oyna""",
        "saski_cmd_frnd_btn": """🤝 Arkadaşla Oyna""",
        "saski_btn_bot": """🤖 Botla Oyna""",
        "saski_btn_friend": """🤝 Arkadaşla Oyna""",
        "saski_menu_text": """⛀⛂ <b>Saski — Mod Seçin</b>

🤖 <b>Botla</b> — Pratik yap, ELO etkilenmez
🤝 <b>Arkadaş</b> — Renk seç ve birlikte oyna""",
        "err_game_not_found": """⚠️ Oyun bulunamadı. Lütfen yeni bir davet gönderin.""",
        "draw_bot_not_allowed": """🤖 Bu bir bot oyunudur — bot beraberliği kabul edemez.
Ya kazan ya kaybet! 💪""",
        "friend_pick_color_title": """🎮 <b>Arkadaş Oyunu — Renk Seç</b>""",
        "friend_pick_color_text": """🎮 <b>Arkadaş Oyunu</b>

Rengini seç, rakibin diğerini alsın:

⚪ Beyaz — ilk hamle
⚫ Siyah — ikinci hamle

⚪ Beyaz: {white}
⚫ Siyah: {black}""",
        "piece_selected": """✅ Taş seçildi, şimdi hedef kareyi seçin""",
        "friend_lang_btn": """🌍 Oyun Dilini Seç""",
        "friend_game_over_shared": """🏁 <b>Oyun bitti.</b>
{result}""",
        "mode_bot": """Botla""",
        "mode_pvp": """Çevrimiçi""",
        "mode_friend": """Arkadaşla""",
        "err_not_your_turn": """⛔ Sıra sizde değil! Rakibinizi bekleyin.""",
        "err_invalid_move": """❌ Bu hamleye izin verilmiyor. Farklı bir kare seçin.""",
        "err_must_jump": """⚠️ Bir yeme durumu var! Taş yemelisiniz — normal hamleler yasaktır.""",
        "err_chain_jump": """🔗 Zincirleme yeme mümkün! Zıplamaya devam edebilirsiniz — diziyi tamamlayın.""",
        "err_king_must_jump": """👑 Taşınızın yeme imkanı var! Taş yemek zorunludur.""",
        "err_man_no_backward": """🚫 Normal taşlar geri gidemez! Sadece ileri (ancak geriye yiyebilir).""",
        "err_no_piece_here": """🔍 Burada taşınız yok. Kendi taşınıza dokunun.""",
        "err_already_in_game": """🎮 Zaten devam eden bir oyununuz var! Yeni bir tane başlatmadan önce bitirin.""",
        "err_king_promoted_chain": """👑⚡ Taş dama oldu! Şimdi tüm yenebilir rakip taşlarını almalısınız!""",
        "timeout_winner": """⏲️ <b>Oyun Bitti — Kazanan: {winner}!</b>
{loser} süreyi bitirdi.

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "timeout_loser": """⏲️ <b>Ойын аяқталды — {winner} жеңді!</b>
{loser} уақытты асырды.

📈 <b>Нәтиже:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})""",
        "draw_offer_sent": """🤝 Beraberlik teklifi gönderildi. Yanıt bekleniyor…""",
        "draw_already_offered": """ℹ️ Zaten bir beraberlik teklif ettiniz. Rakibin yanıtını bekleyin.""",
        "draw_offer_recv": """🤝 <b>Rakibiniz beraberlik teklif etti!</b>
Kabul ediyor musunuz?""",
        "draw_accept_btn": """✅ Kabul Et""",
        "draw_reject_btn": """❌ Reddet""",
        "draw_accepted_white": """🤝 <b>Oyun Bitti — Beraberlik!</b>

📈 <b>Sonuçlar:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun için /saski""",
        "draw_accepted_black": """🤝 <b>Oyun Bitti — Beraberlik!</b>

📈 <b>Sonuçlar:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun için /saski""",
        "draw_rejected_by_you": """❌ Beraberliği reddettiniz. Oyun kaldığı yerden devam ediyor.""",
        "draw_rejected_notif": """❌ Rakibiniz beraberliği reddetti. Oyun devam ediyor!""",
        "no_opponent_yet": """⏳ Henüz rakip yok. Birinin katılmasını bekleyin.""",
        "not_participant": """🚫 Bu oyunun katılımcısı değilsiniz!""",
        "surrender_winner": """🏳️ <b>Oyun Bitti — Kazanan: {winner}!</b>
{loser} teslim oldu. 🎉 Tebrikler!

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "surrender_loser": """🏳️ <b>Oyun Bitti — Kazanan: {winner}!</b>
Teslim oldunuz.

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "game_over_hint": """

🔄 Yeni oyun: /start""",
        "searching": """🔍 <b>Çevrimiçi rakip aranıyor…</b>

Lütfen bekleyin.""",
        "cancel_search_btn": """❌ Aramayı İptal Et""",
        "search_cancelled": """✅ Arama iptal edildi.""",
        "already_searching": """ℹ️ Zaten arama kuyruğundasınız.""",
        "match_found_white": """🎮 <b>Rakip bulundu! Oyun başlıyor!</b>

Siz: ⚪ Beyaz
Hamle sizin, iyi şanslar!

""",
        "match_found_black": """🎮 <b>Rakip bulundu! Oyun başlıyor!</b>

Siz: ⚫ Siyah
Rakibin hamlesini bekleyin.

""",
        "bot_game_start": """🤖 <b>Bot oyunu başladı!</b>

Siz: ⚪ Beyaz
Bot: ⚫ Siyah

Hamle sizin! Bol şans! 🍀

""",
        "inline_title": """⚪⚫ Dama oyunu gönder!""",
        "inline_desc": """Botla veya Arkadaşla — tahta doğrudan bu sohbete gelir""",
        "inline_no_lang_btn": """👉 Bota git, dil seç →""",
        "inline_no_lang_msg": """Önce @SaskiGameBot'a /start gönderip dil seçin — sonra satır içi oyun gönderebilirsiniz!""",
        "group_color_select_msg": """🎮 <b>Saski — Grup Oyunu</b>

Her oyuncu rengini seçsin:

⚪ Beyaz — ilk hamle
⚫ Siyah — ikinci hamle

⚪ Beyaz: {white}
⚫ Siyah: {black}""",
        "group_select_lang_btn": """🌍 Dil Seç""",
        "group_lang_changed": """✅ Oyun dili değiştirildi.""",
        "group_waiting_color": """— bekleniyor —""",
        "friend_invite_title": """🎮 Saski — Arkadaşla Oyna""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Saski — Arkadaş Oyunu</b>

Aşağıdan rengini seç!
İlk tıklayan o rengi alır, ikinci kalanı alır.

⚪ Beyaz — ilk hamle
⚫ Siyah — ikinci hamle""",
        "friend_join_white_btn": """⚪ Beyaz olarak oyna""",
        "friend_join_black_btn": """⚫ Siyah olarak oyna""",
        "friend_color_taken": """⚠️ O renk alındı! Diğerini seçin.""",
        "friend_game_starting": """🎮 İki oyuncu da katıldı! Oyun başlıyor…""",
        "friend_you_white": """⚪ Beyaz rengini seçtiniz!""",
        "friend_you_black": """⚫ Siyah rengini seçtiniz!""",
        "friend_self_join": """⚠️ Kendinize karşı oynayamazsınız! Bir arkadaşınızı davet edin.""",
        "game_over_winner": """🏳️ <b>Oyun Bitti — Kazanan: {winner}!</b>
🎉 Tebrikler!

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "game_over_loser": """🏳️ <b>Oyun Bitti — Kazanan: {winner}!</b>
Kaybettiniz.

📈 <b>Sonuçlar:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})

👇 Yeni oyun için /saski""",
        "game_over_draw": """🤝 <b>Oyun Bitti — Beraberlik!</b>

📈 <b>Sonuçlar:</b>
⚪️ <b>{winner}:</b> {w_old} → {w_new} ({w_diff})
⚫️ <b>{loser}:</b> {l_old} → {l_new} ({l_diff})

👇 Yeni oyun için /saski""",
        "bot_game_over_winner": """🏳️ <b>Bot Oyunu Bitti — Kazanan: {winner}!</b>
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "bot_game_over_loser": """🏳️ <b>Bot Oyunu Bitti — Kazanan: {winner}!</b>
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "surrender_winner_bot": """🏳️ <b>Bot Oyunu Bitti — Kazanan: {winner}!</b>
Bot teslim oldu.
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "surrender_loser_bot": """🏳️ <b>Bot Oyunu Bitti — Kazanan: Bot!</b>
Teslim oldunuz.
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "timeout_winner_bot": """⏲️ <b>Bot Oyunu Bitti — Kazanan: {winner}!</b>
Bot süreyi bitirdi.
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "timeout_loser_bot": """⏲️ <b>Bot Oyunu Bitti — Kazanan: Bot!</b>
Süreniz bitti.
ℹ️ Bot oyunları istatistikleri etkilemez.

👇 Yeni oyun için /saski""",
        "broadcast_no_perm": """🚫 Bu komut sadece yöneticiler içindir.""",
        "broadcast_no_reply": """⚠️ Yayınlamak için bir mesaja yanıt verin.""",
        "broadcast_done": """✅ Yayın tamamlandı: {ok} kişi, {fail} başarısız.""",
        "group_game_start": """🎮 <b>Grupta Saski oyunu başladı!</b>

Sadece kendi sıranızda hamle yapın.""",
        "draw_is_your_offer": """ℹ️ Bu kendi beraberlik teklifiniz. Rakibin yanıtını bekleyin.""",
        "inline_bot_group_note": """🤖 Bot oyunu başladı! Sadece siz hamle yapabilirsiniz.""",
    },
    "kk": {
        "select_language": """🌍 <b>Тілді таңдаңыз / Тілді таңда / Выберите язык</b>""",
        "lang_selected": """✅ Қазақ тілі таңдалды!""",
        "start_text": """⛀⛂ <b>Дойбы Ботына қош келдіңіз!</b>

🎯 Классикалық 8x8 дойбы — ботпен, онлайн немесе доспен!
🏆 ELO рейтингілік жүйе • ⚡ Нақты уақыттағы жүрістер • ⏲️ Әр жүріске 60 сек

📖 Толық ережелер: /help
👇 Мәзірден режимді таңдаңыз:""",
        "info": """⛀⛂ <b>Дойбы Ботына қош келдіңіз!</b>

🎯 Классикалық 8x8 дойбы — ботпен, онлайн немесе доспен!
🏆 ELO рейтингілік жүйе • ⚡ Нақты уақыттағы жүрістер • ⏲️ Әр жүріске 60 сек

📖 Толық ережелер: /help
👇 Мәзірден режимді таңдаңыз:""",
        "btn_profile": """👤 Менің профилім""",
        "btn_bot": """🤖 Ботпен ойнау""",
        "btn_online": """🌐 Онлайн ойнау""",
        "btn_friend": """🤝 Доспен ойнау""",
        "btn_rating": """🏆 Рейтинг кестесі""",
        "btn_other_bots": """📢 Біздің канал""",
        "btn_add_group": """➕ Топқа қосу""",
        "btn_change_lang": """🌍 Тілді өзгерту""",
        "btn_back": """🔙 Артқа""",
        "btn_surrender": """🏳️ Берілу""",
        "btn_draw": """🤝 Тең ойын""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Рейтингі: {elo}

📊 Барлық ойын: {total_games}
🏆 Жеңіс: {wins}
💔 Жеңіліс: {losses}
🤝 Тең ойын: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Толық нұсқаулық</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Командалар:</b>
• /start — Боты бастау / мәзірге оралу
• /saski — Ойын мәзірі
• /my — Статистика
• /rating — Рейтингтер
• /language — Тілді ауыстыру

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Ережелер:</b>
• ⚪ Ақтар жоғары, ⚫ Қаралар төмен жүреді
• Қарапайым тас тек алға жүреді — бірақ АРТҚА ҚАРАЙ ЖЕЙ АЛАДЫ
• Соңғы қатарға жеткен тас → дамка болады
• 👑 Дамка: 4 бағытқа да еркін жүреді
• ⚡ Жейтін тас болса, жеу МІНДЕТТІ
• 🔗 Тізбектей жеу: бір жүрісте бірнеше тасты алуға болады
• 👑➡⚡ Дамка болғаннан кейін жеу мүмкіндігі болса, тоқтамай жеу керек!
• Барлық қарсылас тастары жойылса немесе бұғатталса → СІЗ ЖЕҢДІҢІЗ!
• ⏲️ Әр жүріске 60 секунд — уақыт бітсе, жеңілесіз!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Режимдер:</b>
• 🤖 <b>Ботпен</b> — Ботпен жаттығу (ELO әсер етпейді)
• 🌐 <b>Онлайн</b> — Кезекке тұрып, қарсылас іздеу
• 🤝 <b>Доспен</b> — Достық кездесу

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO жүйесі:</b>
• Жеңсең: ұпай қосылады   • Жеңілсең: ұпай азаяды
• Ботпен ойын рейтингке әсер етпейді.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Рейтинг мәзірі</b>

Қандай тізімді көргіңіз келеді?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Жеңіс""",
        "top_elo_title": """🏅 <b>TOP 20 — ЕҢ ЖОҒАРЫ ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — ЕҢ КӨП ЖЕҢІС</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} жеңіс
""",
        "turn_white": """Кезек: ⚪ <b>{name}</b>  ⏲️ {sec}с""",
        "turn_black": """Кезек: ⚫ <b>{name}</b>  ⏲️ {sec}с""",
        "board_header": """⛀⛂ <b>Шашки</b> — {mode}

⚪ Ақ: <b>{white}</b>
⚫ Қара: <b>{black}</b>

""",
        "waiting_player": """күтуде…""",
        "bot_label": """Бот 🤖""",
        "saski_cmd_menu": """<b>Шашки</b> — Режим таңдаңыз:""",
        "saski_cmd_bot_btn": """🤖 Ботпен ойнау""",
        "saski_cmd_frnd_btn": """🤝 Доспен ойнау""",
        "saski_btn_bot": """🤖 Ботпен ойнау""",
        "saski_btn_friend": """🤝 Доспен ойнау""",
        "saski_menu_text": """⛀⛂ <b>Шашки — Режим таңдаңыз</b>

🤖 <b>Ботпен</b> — Жаттығу
🤝 <b>Доспен</b> — Досыңмен ойна""",
        "err_game_not_found": """⚠️ Ойын табылмады.""",
        "draw_bot_not_allowed": """🤖 Ботпен ойнағанда тең ойын мүмкін емес.""",
        "friend_pick_color_title": """🎮 <b>Доспен ойын — Түс таңдаңыз</b>""",
        "friend_pick_color_text": """🎮 <b>Достық ойын</b>

Түсіңізді таңдаңыз:

⚪ Ақ — бірінші жүреді
⚫ Қара — екінші жүреді

⚪ Ақ: {white}
⚫ Қара: {black}""",
        "piece_selected": """✅ Тас таңдалды. Жүретін орынды таңдаңыз""",
        "friend_lang_btn": """🌍 Тілді таңдау""",
        "friend_game_over_shared": """🏁 <b>Ойын аяқталды.</b>
{result}""",
        "mode_bot": """Ботпен""",
        "mode_pvp": """Онлайн""",
        "mode_friend": """Доспен""",
        "err_not_your_turn": """⛔ Кезек сіздікі емес!""",
        "err_invalid_move": """❌ Бұл жүріс рұқсат етілмейді.""",
        "err_must_jump": """⚠️ Жеуге болатын тас бар! Жеу керек.""",
        "err_chain_jump": """🔗 Тізбектеп жеуге болады!""",
        "err_king_must_jump": """👑 Дамкамен жеу қажет!""",
        "err_man_no_backward": """🚫 Қарапайым тас артқа жүре алмайды!""",
        "err_no_piece_here": """🔍 Мұнда сіздің тасыңыз жоқ.""",
        "err_already_in_game": """🎮 Сіз басқа ойындасыз!""",
        "err_king_promoted_chain": """👑⚡ Дамка болдыңыз! Енді жеу керек!""",
        "timeout_winner": """⏲️ <b>Ойын аяқталды — {winner} жеңді!</b>
{loser} уақытты асырды.

📈 <b>Нәтиже:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})""",
        "timeout_loser": """⏲️ <b>Оюн аяктады — {winner} жеңди!</b>
{loser} убакытты ашырды.""",
        "draw_offer_sent": """🤝 Тең ойын ұсынылды.""",
        "draw_already_offered": """ℹ️ Ұсыныс жасалған.""",
        "draw_offer_recv": """🤝 <b>Тең ойын ұсынылды!</b>
Қабылдайсыз ба?""",
        "draw_accept_btn": """✅ Иә""",
        "draw_reject_btn": """❌ Жоқ""",
        "draw_accepted_white": """🤝 <b>Ойын тең аяқталды!</b>""",
        "draw_accepted_black": """🤝 <b>Ойын тең аяқталды!</b>""",
        "draw_rejected_by_you": """❌ Қарсылас ұсынысты қабылдамады.""",
        "draw_rejected_notif": """❌ Қарсылас ұсынысты қабылдамады.""",
        "no_opponent_yet": """⏳ Қарсылас күтілуде.""",
        "not_participant": """🚫 Ойыншы емессіз!""",
        "surrender_winner": """🏳️ <b>Ойын аяқталды — {winner} жеңді!</b>""",
        "surrender_loser": """🏳️ <b>Ойын аяқталды — {winner} жеңді!</b>""",
        "game_over_hint": """

🔄 Жаңа ойын: /start""",
        "searching": """🔍 <b>Қарсылас ізделуде…</b>""",
        "cancel_search_btn": """❌ Тоқтату""",
        "search_cancelled": """✅ Іздеу тоқтатылды.""",
        "already_searching": """ℹ️ Іздеудесіз.""",
        "match_found_white": """🎮 <b>Ойын басталды!</b>

Сіз: ⚪ Ақ""",
        "match_found_black": """🎮 <b>Ойын басталды!</b>

Сіз: ⚫ Қара""",
        "bot_game_start": """🤖 <b>Ботпен ойын басталды!</b>""",
        "inline_title": """⚪⚫ Шашки ойнау!""",
        "inline_desc": """Доспен немесе ботпен ойнаңыз""",
        "inline_no_lang_btn": """👉 Ботқа өтіңіз""",
        "inline_no_lang_msg": """Алдымен боттан тіл таңдаңыз.""",
        "group_color_select_msg": """🎮 <b>Топтық ойын</b>""",
        "group_select_lang_btn": """🌍 Тіл""",
        "group_lang_changed": """✅ Тіл өзгертілді.""",
        "group_waiting_color": """— күтуде —""",
        "friend_invite_title": """🎮 Шашки — Доспен ойнау""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Достық ойын</b>

Түс таңдаңыз!""",
        "friend_join_white_btn": """⚪ Ақ болу""",
        "friend_join_black_btn": """⚫ Қара болу""",
        "friend_color_taken": """⚠️ Бұл түс алынған.""",
        "friend_game_starting": """🎮 Ойын басталды…""",
        "friend_you_white": """⚪ Ақсыңыз!""",
        "friend_you_black": """⚫ Қарасыз!""",
        "friend_self_join": """⚠️ Өзіңізге қарсы ойнай алмайсыз!""",
        "game_over_winner": """🏳️ <b>Ойын аяқталды!</b>""",
        "game_over_loser": """🏳️ <b>Ойын аяқталды!</b>""",
        "game_over_draw": """🤝 <b>Тең ойын!</b>""",
        "bot_game_over_winner": """🏳️ <b>Ботпен ойын аяқталды!</b>""",
        "bot_game_over_loser": """🏳️ <b>Ботпен ойын аяқталды!</b>""",
        "surrender_winner_bot": """🏳️ <b>Ботпен ойын аяқталды!</b>""",
        "surrender_loser_bot": """🏳️ <b>Ботпен ойын аяқталды!</b>""",
        "timeout_winner_bot": """⏲️ <b>Ботпен ойын аяқталды!</b>""",
        "timeout_loser_bot": """⏲️ <b>Ботпен ойын аяқталды!</b>""",
        "broadcast_no_perm": """🚫 Әкімші құқығы қажет.""",
        "broadcast_no_reply": """⚠️ Хабарламаны сұрыптаңыз.""",
        "broadcast_done": """✅ Жіберілді.""",
        "group_game_start": """🎮 <b>Ойын басталды!</b>""",
        "draw_is_your_offer": """ℹ️ Ұсыныс жасалған.""",
        "inline_bot_group_note": """🤖 Бот ойыны.""",
    },
    "ky": {
        "select_language": """🌍 <b>Тилди тандаңыз / Тилди танда / Выберите язык</b>""",
        "lang_selected": """✅ Кыргыз тили тандалды!""",
        "start_text": """⛀⛂ <b>Дойбу Ботуна кош келдиңиз!</b>

🎯 Классикалык 8x8 дойбу — бот менен, онлайн же дос менен!
🏆 ELO рейтингтик системасы • ⚡ Реалдуу убакыттагы жүрүштөр • ⏲️ Ар бир жүрүшкө 60 сек

📖 Толук эрежелер: /help
👇 Менюдан режимди тандаңыз:""",
        "info": """⛀⛂ <b>Дойбу Ботуна кош келдиңиз!</b>

🎯 Классикалык 8x8 дойбу — бот менен, онлайн же дос менен!
🏆 ELO рейтингтик системасы • ⚡ Реалдуу убакыттагы жүрүштөр • ⏲️ Ар бир жүрүшкө 60 сек

📖 Толук эрежелер: /help
👇 Менюдан режимди тандаңыз:""",
        "btn_profile": """👤 Менин профилим""",
        "btn_bot": """🤖 Бот менен ойноо""",
        "btn_online": """🌐 Онлайн ойноо""",
        "btn_friend": """🤝 Дос менен ойноо""",
        "btn_rating": """🏆 Рейтинг таблицасы""",
        "btn_other_bots": """📢 Биздин канал""",
        "btn_add_group": """➕ Топко кошуу""",
        "btn_change_lang": """🌍 Тилди өзгөртүү""",
        "btn_back": """🔙 Артка""",
        "btn_surrender": """🏳️ Багынуу""",
        "btn_draw": """🤝 Тең оюн""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Рейтинги: {elo}

📊 Бардык оюндар: {total_games}
🏆 Жеңиш: {wins}
💔 Жеңилүү: {losses}
🤝 Тең оюн: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Толук колдонмо</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Командалар:</b>
• /start — Боту баштоо / менюга кайтуу
• /saski — Оюн менюсу
• /my — Статистика
• /rating — Рейтингдер
• /language — Тилди өзгөртүү

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Эрежелер:</b>
• ⚪ Актар өйдө, ⚫ Каралар ылдый жүрөт
• Жөнөкөй таш алдыга гана жүрөт — бирок АРТКА ЖЕЙ АЛАТ
• Акыркы катардагы таш → дамка болот
• 👑 Дамка: 4 багытка тең эркин жүрөт
• ⚡ Жей турган таш болсо, жеш МИЛДЕТТҮҮ
• 🔗 Тизмектеп жеш: бир жүрүштө бир нече ташты алат
• 👑➡⚡ Дамка болгондон кийин жеш мүмүнчүлүгү болсо, токтобой жеш керек!
• Бардык атаандаш таштары жок кылынса же блоктолсо → СИЗ ЖЕҢДИҢИЗ!
• ⏲️ Ар бир жүрүшкө 60 секунд — убакыт бүтсө, жеңилесиз!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Режимдер:</b>
• 🤖 <b>Бот менен</b> — Машыгуу (ELO таасир этпейт)
• 🌐 <b>Онлайн</b> — Кезекке туруп, атаандаш издөө
• 🤝 <b>Дос менен</b> — Достук оюн

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO системасы:</b>
• Жеңсең: упай кошулат   • Жеңилсең: упай азаят
• Бот менен оюн рейтингге таасир этпейт.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Рейтинг менюсу</b>

Кайсы тизмени көргүңүз келет?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Жеңиш""",
        "top_elo_title": """🏅 <b>TOP 20 — ЭҢ ЖОГОРКУ ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — ЭҢ КӨП ЖЕҢИШ</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} жеңиш
""",
        "turn_white": """Кезек: ⚪ <b>{name}</b>  ⏲️ {sec}с""",
        "turn_black": """Кезек: ⚫ <b>{name}</b>  ⏲️ {sec}с""",
        "board_header": """⛀⛂ <b>Шашки</b> — {mode}

⚪ Актар: <b>{white}</b>
⚫ Каралар: <b>{black}</b>

""",
        "waiting_player": """күтүүдө…""",
        "bot_label": """Бот 🤖""",
        "saski_cmd_menu": """<b>Шашки</b> — Режим тандаңыз:""",
        "saski_cmd_bot_btn": """🤖 Бот менен ойноо""",
        "saski_cmd_frnd_btn": """🤝 Дос менен ойноо""",
        "saski_btn_bot": """🤖 Бот менен ойноо""",
        "saski_btn_friend": """🤝 Дос менен ойноо""",
        "saski_menu_text": """⛀⛂ <b>Шашки — Режим тандаңыз</b>

🤖 <b>Бот менен</b> — Машыгуу
🤝 <b>Дос менен</b> — Досуң менен ойно""",
        "err_game_not_found": """⚠️ Оюн табылган жок.""",
        "draw_bot_not_allowed": """🤖 Бот менен тең оюн мүмкүн эмес.""",
        "friend_pick_color_title": """🎮 <b>Дос менен оюн — Түс тандаңыз</b>""",
        "friend_pick_color_text": """🎮 <b>Достук оюн</b>

Түсүңүздү тандаңыз:

⚪ Актар — биринчи жүрөт
⚫ Каралар — экинчи жүрөт

⚪ Актар: {white}
⚫ Каралар: {black}""",
        "piece_selected": """✅ Таш тандалды.""",
        "friend_lang_btn": """🌍 Тилди тандоо""",
        "friend_game_over_shared": """🏁 <b>Оюн аяктады.</b>
{result}""",
        "mode_bot": """Бот менен""",
        "mode_pvp": """Онлайн""",
        "mode_friend": """Дос менен""",
        "err_not_your_turn": """⛔ Кезек сиздики эмес!""",
        "err_invalid_move": """❌ Бул жүрүшкө болбойт.""",
        "err_must_jump": """⚠️ Жеш керек!""",
        "err_chain_jump": """🔗 Тизмектеп жеш мүмкүн!""",
        "err_king_must_jump": """👑 Дамка менен жеш милдеттүү!""",
        "err_man_no_backward": """🚫 Таш артка жүрө албайт!""",
        "err_no_piece_here": """🔍 Ташыңыз жок.""",
        "err_already_in_game": """🎮 Оюнду бүтүрүңүз!""",
        "err_king_promoted_chain": """👑⚡ Дамка болдуңуз! Жеш керек!""",
        "timeout_winner": """⏲️ <b>Оюн аяктады — {winner} жеңди!</b>
{loser} убакытты ашырды.""",
        "timeout_loser": """⏲️ <b>गेम ओवर — {winner} की जीत!</b>
{loser} का समय खत्म।

📈 <b>परिणाम:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})""",
        "draw_offer_sent": """🤝 Сунуш жиберилди.""",
        "draw_already_offered": """ℹ️ Сунуш жиберилген.""",
        "draw_offer_recv": """🤝 <b>Тең оюн сунушталууда!</b>""",
        "draw_accept_btn": """✅ Ооба""",
        "draw_reject_btn": """❌ Жок""",
        "draw_accepted_white": """🤝 <b>Тең оюн!</b>""",
        "draw_accepted_black": """🤝 <b>Тең оюн!</b>""",
        "draw_rejected_by_you": """❌ Атаандаш баш тартты.""",
        "draw_rejected_notif": """❌ Атаандаш баш тартты.""",
        "no_opponent_yet": """⏳ Атаандаш күтүлүүдө.""",
        "not_participant": """🚫 Оюнчу эмессиз!""",
        "surrender_winner": """🏳️ <b>Оюн аяктады — {winner} жеңди!</b>""",
        "surrender_loser": """🏳️ <b>Оюн аяктады — {winner} жеңди!</b>""",
        "game_over_hint": """

🔄 Жаңы оюн: /start""",
        "searching": """🔍 <b>Издөө…</b>""",
        "cancel_search_btn": """❌ Токтотуу""",
        "search_cancelled": """✅ Издөө токтотулду.""",
        "already_searching": """ℹ️ Издөөдөсүз.""",
        "match_found_white": """🎮 <b>Оюн башталды!</b>

Сиз: ⚪ Актар""",
        "match_found_black": """🎮 <b>Оюн башталды!</b>

Сиз: ⚫ Каралар""",
        "bot_game_start": """🤖 <b>Бот менен оюн!</b>""",
        "inline_title": """⚪⚫ Шашки!""",
        "inline_desc": """Дос же бот менен.""",
        "inline_no_lang_btn": """👉 Ботко өтүңүз""",
        "inline_no_lang_msg": """Тил тандаңыз.""",
        "group_color_select_msg": """🎮 <b>Топтук оюн</b>""",
        "group_select_lang_btn": """🌍 Тил""",
        "group_lang_changed": """✅ Тил өзгөртүлдү.""",
        "group_waiting_color": """— күтүүдө —""",
        "friend_invite_title": """🎮 Шашки — Дос менен""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Достук оюн</b>

Түс тандаңыз!""",
        "friend_join_white_btn": """⚪ Актар""",
        "friend_join_black_btn": """⚫ Каралар""",
        "friend_color_taken": """⚠️ Түс алынган.""",
        "friend_game_starting": """🎮 Оюн башталды…""",
        "friend_you_white": """⚪ Актарсыз!""",
        "friend_you_black": """⚫ Караларсыз!""",
        "friend_self_join": """⚠️ Өзүңүзгө каршы ойнобойсуз!""",
        "game_over_winner": """🏳️ <b>Оюн аяктады!</b>""",
        "game_over_loser": """🏳️ <b>Оюн аяктады!</b>""",
        "game_over_draw": """🤝 <b>Тең оюн!</b>""",
        "bot_game_over_winner": """🏳️ <b>Оюн бүттү!</b>""",
        "bot_game_over_loser": """🏳️ <b>Оюн бүттү!</b>""",
        "surrender_winner_bot": """🏳️ <b>Оюн бүттү!</b>""",
        "surrender_loser_bot": """🏳️ <b>Оюн бүттү!</b>""",
        "timeout_winner_bot": """⏲️ <b>Оюн бүттү!</b>""",
        "timeout_loser_bot": """⏲️ <b>Оюн бүттү!</b>""",
        "broadcast_no_perm": """🚫 Админ гана.""",
        "broadcast_no_reply": """⚠️ Жооп бериңиз.""",
        "broadcast_done": """✅ Жиберилди.""",
        "group_game_start": """🎮 <b>Оюн башталды!</b>""",
        "draw_is_your_offer": """ℹ️ Ұсыныс жасалган.""",
        "inline_bot_group_note": """🤖 Бот менен.""",
    },
    "hi": {
        "select_language": """🌍 <b>भाषा चुनें / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ अंग्रेज़ी चुनी गई!""",
        "start_text": """⛀⛂ <b>चेकर्स बॉट में आपका स्वागत है!</b>

🎯 क्लासिक 8x8 चेकर्स (Checkers) — बॉट, ऑनलाइन, या दोस्तों के साथ!
🏆 ELO रेटिंग सिस्टम • ⚡ रीयल-टाइम चालें • ⏲️ प्रति चाल 60 सेकंड

📖 पूरे नियम: /help
👇 मेनू से एक मोड चुनें:""",
        "info": """⛀⛂ <b>चेकर्स बॉट में आपका स्वागत है!</b>

🎯 क्लासिक 8x8 चेकर्स (Checkers) — बॉट, ऑनलाइन, या दोस्तों के साथ!
🏆 ELO रेटिंग सिस्टम • ⚡ रीयल-टाइम चालें • ⏲️ प्रति चाल 60 सेकंड

📖 पूरे नियम: /help
👇 मेनू से एक मोड चुनें:""",
        "btn_profile": """👤 मेरी प्रोफ़ाइल""",
        "btn_bot": """🤖 बॉट के खिलाफ खेलें""",
        "btn_online": """🌐 ऑनलाइन खेलें""",
        "btn_friend": """🤝 दोस्तों के साथ खेलें""",
        "btn_rating": """🏆 लीडरबोर्ड""",
        "btn_other_bots": """📢 हमारा चैनल""",
        "btn_add_group": """➕ ग्रुप में जोड़ें""",
        "btn_change_lang": """🌍 भाषा बदलें""",
        "btn_back": """🔙 पीछे""",
        "btn_surrender": """🏳️ आत्मसमर्पण (Surrender)""",
        "btn_draw": """🤝 ड्रॉ""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO रेटिंग: {elo}

📊 कुल गेम: {total_games}
🏆 जीत: {wins}
💔 हार: {losses}
🤝 ड्रॉ: {draws}""",
        "help_text": """🎮 <b>Saski Bot — पूरा गाइड</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>कमांड्स:</b>
• /start — बॉट शुरू करें / मेनू पर जाएं
• /saski — गेम मेनू (ग्रुप में भी काम करता है)
• /my — आंकड़े
• /rating — लीडरबोर्ड
• /language — भाषा बदलें

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>नियम:</b>
• ⚪ सफेद ऊपर, ⚫ काला नीचे चलता है
• साधारण गोटियाँ: केवल आगे चलती हैं, लेकिन पीछे की ओर भी मार सकती हैं (कैप्चर करना)
• आखिरी कतार में पहुँचने पर → किंग (क्वीन) बन जाती है
• 👑 किंग: किसी भी दिशा में और कितनी भी दूर चल सकता है
• ⚡ कैप्चर (मारना) अनिवार्य है
• 🔗 चेन कैप्चर: एक ही बारी में लगातार मारते रहना
• 👑➡⚡ किंग बनने के तुरंत बाद मारना संभव है? तो करना ही होगा!
• विपक्षी गोटियाँ खत्म या ब्लॉक → आप जीत गए!
• ⏲️ 60 सेकंड/चाल!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>मोड्स:</b>
• 🤖 <b>बॉट</b> — अभ्यास करें
• 🌐 <b>ऑनलाइन</b> — रैंडम खिलाड़ी
• 🤝 <b>मित्र</b> — दोस्तों के साथ

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO प्रणाली:</b>
• जीत: रेटिंग ऊपर   • हार: रेटिंग नीचे
• बॉट गेम ELO को प्रभावित नहीं करते।

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>लीडरबोर्ड मेनू</b>

कौन सी सूची देखना चाहते हैं?""",
        "btn_top_elo": """🥇 टॉप 20 ELO""",
        "btn_top_wins": """⚔️ टॉप 20 जीत""",
        "top_elo_title": """🏅 <b>टॉप 20 — उच्चतम ELO</b>

""",
        "top_wins_title": """⚔️ <b>टॉप 20 — सबसे अधिक जीत</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} जीत
""",
        "turn_white": """चाल: ⚪ <b>{name}</b>  ⏲️ {sec}s""",
        "turn_black": """चाल: ⚫ <b>{name}</b>  ⏲️ {sec}s""",
        "board_header": """⛀⛂ <b>Checkers</b> — {mode}

⚪ सफेद: <b>{white}</b>
⚫ काला: <b>{black}</b>

""",
        "waiting_player": """प्रतीक्षा में…""",
        "bot_label": """बॉट 🤖""",
        "saski_cmd_menu": """<b>Saski</b> — मोड चुनें:""",
        "saski_cmd_bot_btn": """🤖 बॉट के खिलाफ""",
        "saski_cmd_frnd_btn": """🤝 दोस्तों के साथ""",
        "saski_btn_bot": """🤖 बॉट के खिलाफ""",
        "saski_btn_friend": """🤝 दोस्तों के साथ""",
        "saski_menu_text": """⛀⛂ <b>Saski — मोड चुनें</b>

🤖 <b>बॉट</b> — अभ्यास
🤝 <b>मित्र</b> — दोस्तों के साथ खेलें""",
        "err_game_not_found": """⚠️ गेम नहीं मिला।""",
        "draw_bot_not_allowed": """🤖 बॉट ड्रॉ नहीं स्वीकारते।""",
        "friend_pick_color_title": """🎮 <b>मित्र गेम — रंग चुनें</b>""",
        "friend_pick_color_text": """🎮 <b>मित्र गेम</b>

रंग चुनें:

⚪ सफेद — पहली चाल
⚫ काला — दूसरी चाल

⚪ सफेद: {white}
⚫ काला: {black}""",
        "piece_selected": """✅ गोटी चुनी गई, अब गंतव्य चुनें""",
        "friend_lang_btn": """🌍 भाषा चुनें""",
        "friend_game_over_shared": """🏁 <b>गेम समाप्त।</b>
{result}""",
        "mode_bot": """बॉट""",
        "mode_pvp": """ऑनलाइन""",
        "mode_friend": """मित्र""",
        "err_not_your_turn": """⛔ आपकी बारी नहीं है!""",
        "err_invalid_move": """❌ यह चाल अवैध है।""",
        "err_must_jump": """⚠️ मारना (Jump) जरूरी है!""",
        "err_chain_jump": """🔗 चेन जंप संभव है!""",
        "err_king_must_jump": """👑 किंग को मारना जरूरी है!""",
        "err_man_no_backward": """🚫 साधारण गोटी पीछे नहीं चल सकती!""",
        "err_no_piece_here": """🔍 यहाँ आपकी गोटी नहीं है।""",
        "err_already_in_game": """🎮 आप पहले से गेम में हैं!""",
        "err_king_promoted_chain": """👑⚡ किंग बन गए! अब कैप्चर करना होगा!""",
        "timeout_winner": """⏲️ <b>गेम ओवर — {winner} की जीत!</b>
{loser} का समय खत्म।

📈 <b>परिणाम:</b>
{w_icon} <b>{winner}:</b> {w_old} → {w_new} (+{w_diff})
{l_icon} <b>{loser}:</b> {l_old} → {l_new} (-{l_diff})""",
        "timeout_loser": """⏲️ <b>O'yin tugadi — {winner} yutdi!</b>
{loser} vaqtni cho'zdi.""",
        "draw_offer_sent": """🤝 ड्रॉ का प्रस्ताव दिया।""",
        "draw_already_offered": """ℹ️ आपने पहले ही ड्रॉ प्रस्तावित किया है।""",
        "draw_offer_recv": """🤝 <b>ड्रॉ का प्रस्ताव!</b>
स्वीकारें?""",
        "draw_accept_btn": """✅ हाँ""",
        "draw_reject_btn": """❌ नहीं""",
        "draw_accepted_white": """🤝 <b>गेम ड्रॉ!</b>""",
        "draw_accepted_black": """🤝 <b>गेम ड्रॉ!</b>""",
        "draw_rejected_by_you": """❌ ड्रॉ नहीं माना गया।""",
        "draw_rejected_notif": """❌ ड्रॉ नहीं माना गया।""",
        "no_opponent_yet": """⏳ खिलाड़ी की प्रतीक्षा…""",
        "not_participant": """🚫 आप खिलाड़ी नहीं हैं!""",
        "surrender_winner": """🏳️ <b>{winner} की जीत!</b>""",
        "surrender_loser": """🏳️ <b>{winner} की जीत!</b>""",
        "game_over_hint": """

🔄 नया गेम: /start""",
        "searching": """🔍 <b>खिलाड़ी खोजे जा रहे हैं…</b>""",
        "cancel_search_btn": """❌ रद्द करें""",
        "search_cancelled": """✅ खोज बंद हुई।""",
        "already_searching": """ℹ️ आप पहले ही खोज में हैं।""",
        "match_found_white": """🎮 <b>गेम शुरू!</b>

आप: ⚪ सफेद""",
        "match_found_black": """🎮 <b>गेम शुरू!</b>

आप: ⚫ काला""",
        "bot_game_start": """🤖 <b>बॉट गेम शुरू!</b>""",
        "inline_title": """⚪⚫ Checkers!""",
        "inline_desc": """दोस्तों के साथ खेलें""",
        "inline_no_lang_btn": """👉 बॉट पर जाएं""",
        "inline_no_lang_msg": """भाषा चुनें।""",
        "group_color_select_msg": """🎮 <b>ग्रुप गेम</b>""",
        "group_select_lang_btn": """🌍 भाषा""",
        "group_lang_changed": """✅ भाषा बदली गई।""",
        "group_waiting_color": """— प्रतीक्षा —""",
        "friend_invite_title": """🎮 Saski — दोस्तों के साथ""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>मित्र गेम</b>

अपना रंग चुनें!""",
        "friend_join_white_btn": """⚪ सफेद""",
        "friend_join_black_btn": """⚫ काला""",
        "friend_color_taken": """⚠️ यह रंग चु लिया गया है।""",
        "friend_game_starting": """🎮 गेम शुरू…""",
        "friend_you_white": """⚪ सफेद!""",
        "friend_you_black": """⚫ काला!""",
        "friend_self_join": """⚠️ स्वयं के खिलाफ नहीं!""",
        "game_over_winner": """🏳️ <b>गेम ओवर!</b>""",
        "game_over_loser": """🏳️ <b>गेम ओवर!</b>""",
        "game_over_draw": """🤝 <b>गेम ड्रॉ!</b>""",
        "bot_game_over_winner": """🏳️ <b>गेम ओवर!</b>""",
        "bot_game_over_loser": """🏳️ <b>गेम ओवर!</b>""",
        "surrender_winner_bot": """🏳️ <b>गेम ओवर!</b>""",
        "surrender_loser_bot": """🏳️ <b>गेम ओवर!</b>""",
        "timeout_winner_bot": """⏲️ <b>गेम ओवर!</b>""",
        "timeout_loser_bot": """⏲️ <b>गेम ओवर!</b>""",
        "broadcast_no_perm": """🚫 केवल एडमिन।""",
        "broadcast_no_reply": """⚠️ रिप्लाई दें।""",
        "broadcast_done": """✅ हुआ।""",
        "group_game_start": """🎮 <b>गेम शुरू!</b>""",
        "draw_is_your_offer": """ℹ️ प्रस्ताव दिया गया है।""",
        "inline_bot_group_note": """🤖 बॉट गेम।""",
    },
    "uz": {
        "select_language": """🌍 <b>Tilni tanlang / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ Ingliz tili tanlandi!""",
        "start_text": """⛀⛂ <b>Shashka Botiga xush kelibsiz!</b>

🎯 Klassik 8x8 shashka — bot bilan, onlayn yoki do'st bilan!
🏆 ELO reyting tizimi • ⚡ Real vaqtda yurishlar • ⏲️ 60 soniya

📖 Qoidalar: /help
👇 Rejim tanlang:""",
        "info": """⛀⛂ <b>Shashka Botiga xush kelibsiz!</b>

🎯 Klassik 8x8 shashka — bot bilan, onlayn yoki do'st bilan!
🏆 ELO reyting tizimi • ⚡ Real vaqtda yurishlar • ⏲️ 60 soniya

📖 Qoidalar: /help
👇 Rejim tanlang:""",
        "btn_profile": """👤 Profilim""",
        "btn_bot": """🤖 Botga qarshi""",
        "btn_online": """🌐 Onlayn o'yin""",
        "btn_friend": """🤝 Do'st bilan""",
        "btn_rating": """🏆 Reyting""",
        "btn_other_bots": """📢 Kanalimiz""",
        "btn_add_group": """➕ Guruhga qo'shish""",
        "btn_change_lang": """🌍 Tilni o'zgartirish""",
        "btn_back": """🔙 Orqaga""",
        "btn_surrender": """🏳️ Taslim""",
        "btn_draw": """🤝 Durang""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO Reyting: {elo}

📊 Jami o'yinlar: {total_games}
🏆 G'alaba: {wins}
💔 Mag'lubiyat: {losses}
🤝 Durang: {draws}""",
        "help_text": """🎮 <b>Saski Bot — Qo'llanma</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Buyruqlar:</b>
• /start — Botni boshlash
• /saski — O'yin menyusi
• /my — Statistika
• /rating — Top reyting
• /language — Til

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Qoidalar:</b>
• ⚪ Oqlar tepaga, ⚫ Qoralar pastga
• Oddiy tosh faqat oldinga — lekin ORQAGA YEYISH MUMKIN
• Oxiriga yetsa → damka
• 👑 Damka: 4 tomonga erkin yura oladi
• ⚡ Yeyish majburiy
• 🔗 Zanjirsimon yeyish
• 👑➡⚡ Damka bo'ldingizmi? Majburiy yeyish bo'lsa davom eting!
• ⏲️ 60 soniya!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Rejimlar:</b>
• 🤖 <b>Bot</b> — Mashq
• 🌐 <b>Onlayn</b> — Raqib bilan
• 🤝 <b>Do'st</b> — Do'stlaringiz bilan

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO:</b>
• G'alaba: reyting ↑   • Mag'lubiyat: reyting ↓
• Bot reytingga ta'sir qilmaydi.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Reyting menyusi</b>

Qaysi ro'yxatni ko'rmoqchisiz?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 G'alaba""",
        "top_elo_title": """🏅 <b>TOP 20 — Eng yuqori ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — Eng ko'p g'alaba</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} g'alaba
""",
        "turn_white": """Navbat: ⚪ <b>{name}</b>  ⏲️ {sec}s""",
        "turn_black": """Navbat: ⚫ <b>{name}</b>  ⏲️ {sec}s""",
        "board_header": """⛀⛂ <b>Shashka</b> — {mode}

⚪ Oq: <b>{white}</b>
⚫ Qora: <b>{black}</b>

""",
        "waiting_player": """kutilmoqda…""",
        "bot_label": """Bot 🤖""",
        "saski_cmd_menu": """<b>Shashka</b> — Rejim:""",
        "saski_cmd_bot_btn": """🤖 Botga qarshi""",
        "saski_cmd_frnd_btn": """🤝 Do'st bilan""",
        "saski_btn_bot": """🤖 Botga qarshi""",
        "saski_btn_friend": """🤝 Do'st bilan""",
        "saski_menu_text": """⛀⛂ <b>Shashka — Rejim</b>

🤖 <b>Bot</b> — Mashq
🤝 <b>Do'st</b> — Do'stlaringiz bilan""",
        "err_game_not_found": """⚠️ O'yin topilmadi.""",
        "draw_bot_not_allowed": """🤖 Botlar durangni qabul qilmaydi.""",
        "friend_pick_color_title": """🎮 <b>Do'stlar o'yini — Rang</b>""",
        "friend_pick_color_text": """🎮 <b>Do'stlar o'yini</b>

Rangingizni tanlang:

⚪ Oq — birinchi yuradi
⚫ Qora — ikkinchi yuradi

⚪ Oq: {white}
⚫ Qora: {black}""",
        "piece_selected": """✅ Tanlandi, joyni tanlang""",
        "friend_lang_btn": """🌍 Tilni tanlash""",
        "friend_game_over_shared": """🏁 <b>O'yin tugadi.</b>
{result}""",
        "mode_bot": """Bot""",
        "mode_pvp": """Onlayn""",
        "mode_friend": """Do'st""",
        "err_not_your_turn": """⛔ Navbat sizniki emas!""",
        "err_invalid_move": """❌ Bu yurish noto'g'ri.""",
        "err_must_jump": """⚠️ Yeyish majburiy!""",
        "err_chain_jump": """🔗 Zanjirsimon yeyish!""",
        "err_king_must_jump": """👑 Damka yeyishi kerak!""",
        "err_man_no_backward": """🚫 Oddiy tosh orqaga yurmaydi!""",
        "err_no_piece_here": """🔍 Tosh yo'q.""",
        "err_already_in_game": """🎮 Avval o'yinni tugating!""",
        "err_king_promoted_chain": """👑⚡ Damka bo'ldingiz! Yeyish davom etadi!""",
        "timeout_winner": """⏲️ <b>O'yin tugadi — {winner} yutdi!</b>
{loser} vaqtni cho'zdi.""",
        "timeout_loser": """⏲️ <b>انتهت اللعبة — فوز {winner}!</b>
{loser} نفد وقته.""",
        "draw_offer_sent": """🤝 Durang taklif qilindi.""",
        "draw_already_offered": """ℹ️ Taklif qilingan.""",
        "draw_offer_recv": """🤝 <b>Durang taklif etildi!</b>""",
        "draw_accept_btn": """✅ Ha""",
        "draw_reject_btn": """❌ Yo'q""",
        "draw_accepted_white": """🤝 <b>Durang!</b>""",
        "draw_accepted_black": """🤝 <b>Durang!</b>""",
        "draw_rejected_by_you": """❌ Rad etildi.""",
        "draw_rejected_notif": """❌ Rad etildi.""",
        "no_opponent_yet": """⏳ Raqib kutilmoqda.""",
        "not_participant": """🚫 Siz o'yinchi emassiz!""",
        "surrender_winner": """🏳️ <b>O'yin tugadi — {winner} yutdi!</b>""",
        "surrender_loser": """🏳️ <b>O'yin tugadi — {winner} yutdi!</b>""",
        "game_over_hint": """

🔄 Yangi o'yin: /start""",
        "searching": """🔍 <b>Raqib qidirilmoqda…</b>""",
        "cancel_search_btn": """❌ To'xtatish""",
        "search_cancelled": """✅ Qidiruv to'xtatildi.""",
        "already_searching": """ℹ️ Siz allaqachon qidiruvdasiz.""",
        "match_found_white": """🎮 <b>O'yin boshlandi!</b>

Siz: ⚪ Oq""",
        "match_found_black": """🎮 <b>O'yin boshlandi!</b>

Siz: ⚫ Qora""",
        "bot_game_start": """🤖 <b>Bot o'yini boshlandi!</b>""",
        "inline_title": """⚪⚫ Shashka o'ynash!""",
        "inline_desc": """Do'st bilan o'ynang""",
        "inline_no_lang_btn": """👉 Botga o'ting""",
        "inline_no_lang_msg": """Tilni tanlang.""",
        "group_color_select_msg": """🎮 <b>Guruh o'yini</b>""",
        "group_select_lang_btn": """🌍 Til""",
        "group_lang_changed": """✅ Til o'zgartirildi.""",
        "group_waiting_color": """— kutilmoqda —""",
        "friend_invite_title": """🎮 Shashka — Do'st bilan""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Do'stlar o'yini</b>

Rangni tanlang!""",
        "friend_join_white_btn": """⚪ Oq""",
        "friend_join_black_btn": """⚫ Qora""",
        "friend_color_taken": """⚠️ Bu rang band.""",
        "friend_game_starting": """🎮 O'yin boshlandi…""",
        "friend_you_white": """⚪ Oqsiz!""",
        "friend_you_black": """⚫ Qorasiz!""",
        "friend_self_join": """⚠️ O'zingizga qarshi o'ynamang!""",
        "game_over_winner": """🏳️ <b>O'yin tugadi!</b>""",
        "game_over_loser": """🏳️ <b>O'yin tugadi!</b>""",
        "game_over_draw": """🤝 <b>Durang!</b>""",
        "bot_game_over_winner": """🏳️ <b>O'yin tugadi!</b>""",
        "bot_game_over_loser": """🏳️ <b>O'yin tugadi!</b>""",
        "surrender_winner_bot": """🏳️ <b>O'yin tugadi!</b>""",
        "surrender_loser_bot": """🏳️ <b>O'yin tugadi!</b>""",
        "timeout_winner_bot": """⏲️ <b>O'yin tugadi!</b>""",
        "timeout_loser_bot": """⏲️ <b>O'yin tugadi!</b>""",
        "broadcast_no_perm": """🚫 Faqat admin.""",
        "broadcast_no_reply": """⚠️ Javob bering.""",
        "broadcast_done": """✅ Yuborildi.""",
        "group_game_start": """🎮 <b>O'yin boshlandi!</b>""",
        "draw_is_your_offer": """ℹ️ Taklif qilindi.""",
        "inline_bot_group_note": """🤖 Bot o'yini.""",
    },
    "ar": {
        "select_language": """🌍 <b>اختر اللغة / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ تم اختيار اللغة الإنجليزية!""",
        "start_text": """⛀⛂ <b>مرحباً بك في بوت الداما!</b>

🎯 داما كلاسيكية 8x8 — ضد البوت، عبر الإنترنت، أو مع صديق!
🏆 نظام تصنيف ELO • ⚡ تحركات فورية • ⏲️ 60 ثانية لكل دور

📖 القواعد الكاملة: /help
👇 اختر نمط اللعب من القائمة:""",
        "info": """⛀⛂ <b>مرحباً بك في بوت الداما!</b>

🎯 داما كلاسيكية 8x8 — ضد البوت، عبر الإنترنت، أو مع صديق!
🏆 نظام تصنيف ELO • ⚡ تحركات فورية • ⏲️ 60 ثانية لكل دور

📖 القواعد الكاملة: /help
👇 اختر نمط اللعب من القائمة:""",
        "btn_profile": """👤 ملفي الشخصي""",
        "btn_bot": """🤖 اللعب ضد البوت""",
        "btn_online": """🌐 اللعب عبر الإنترنت""",
        "btn_friend": """🤝 اللعب مع صديق""",
        "btn_rating": """🏆 لوحة الصدارة""",
        "btn_other_bots": """📢 قناتنا""",
        "btn_add_group": """➕ إضافة إلى مجموعة""",
        "btn_change_lang": """🌍 تغيير اللغة""",
        "btn_back": """🔙 عودة""",
        "btn_surrender": """🏳️ استسلام""",
        "btn_draw": """🤝 تعادل""",
        "profile_text": """👤 <b>{name}</b>
🏅 تصنيف ELO: {elo}

📊 إجمالي الألعاب: {total_games}
🏆 الفوز: {wins}
💔 الخسارة: {losses}
🤝 التعادل: {draws}""",
        "help_text": """🎮 <b>دليل بوت الداما — Saski</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>الأوامر:</b>
• /start — بدء البوت / العودة للقائمة
• /saski — قائمة الداما
• /my — إحصائياتك
• /rating — قائمة المتصدرين
• /language — تغيير اللغة

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>القواعد:</b>
• ⚪ الأبيض للأعلى، ⚫ الأسود للأسفل
• القطع العادية: تتحرك للأمام فقط — لكن يمكنها الأكل للخلف
• الوصول للصف الأخير → ترقية إلى ملك (دامكا)
• 👑 الملك: يتحرك للأمام وللخلف، بأي مسافة
• ⚡ الأكل إجباري
• 🔗 القفز المتسلسل: استمر في القفز
• 👑➡⚡ أصبحت ملكاً وهناك فرصة للأكل؟ يجب المتابعة فوراً
• ⏲️ 60 ثانية للدور!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>الأنماط:</b>
• 🤖 <b>ضد البوت</b> — للتدريب
• 🌐 <b>أونلاين</b> — ابحث عن خصم
• 🤝 <b>صديق</b> — العب مع صديق

━━━━━━━━━━━━━━━━━━━━
🏆 <b>نظام ELO:</b>
• الفوز: تزيد نقاطك   • الخسارة: تنقص نقاطك
• ألعاب البوت لا تؤثر على التصنيف.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>قائمة المتصدرين</b>

أي قائمة تود عرضها؟""",
        "btn_top_elo": """🥇 أعلى 20 ELO""",
        "btn_top_wins": """⚔️ أعلى 20 فوزاً""",
        "top_elo_title": """🏅 <b>أعلى 20 — تصنيف ELO</b>

""",
        "top_wins_title": """⚔️ <b>أعلى 20 — أكثر فوزاً</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} فوزاً
""",
        "turn_white": """الدور: ⚪ <b>{name}</b>  ⏲️ {sec}ث""",
        "turn_black": """الدور: ⚫ <b>{name}</b>  ⏲️ {sec}ث""",
        "board_header": """⛀⛂ <b>داما</b> — {mode}

⚪ الأبيض: <b>{white}</b>
⚫ الأسود: <b>{black}</b>

""",
        "waiting_player": """بانتظار…""",
        "bot_label": """بوت 🤖""",
        "saski_cmd_menu": """<b>داما</b> — اختر النمط:""",
        "saski_cmd_bot_btn": """🤖 ضد البوت""",
        "saski_cmd_frnd_btn": """🤝 مع صديق""",
        "saski_btn_bot": """🤖 ضد البوت""",
        "saski_btn_friend": """🤝 مع صديق""",
        "saski_menu_text": """⛀⛂ <b>داما — اختر النمط</b>

🤖 <b>ضد البوت</b> — تدريب
🤝 <b>مع صديق</b> — العب معاً""",
        "err_game_not_found": """⚠️ لم يتم العثور على اللعبة.""",
        "draw_bot_not_allowed": """🤖 البوت لا يقبل التعادل.""",
        "friend_pick_color_title": """🎮 <b>لعبة صديق — اختر اللون</b>""",
        "friend_pick_color_text": """🎮 <b>لعبة صديق</b>

اختر لونك:

⚪ الأبيض — يتحرك أولاً
⚫ الأسود — يتحرك ثانياً

⚪ الأبيض: {white}
⚫ الأسود: {black}""",
        "piece_selected": """✅ تم اختيار القطعة.""",
        "friend_lang_btn": """🌍 اختر اللغة""",
        "friend_game_over_shared": """🏁 <b>انتهت اللعبة.</b>
{result}""",
        "mode_bot": """ضد البوت""",
        "mode_pvp": """أونلاين""",
        "mode_friend": """مع صديق""",
        "err_not_your_turn": """⛔ ليس دورك!""",
        "err_invalid_move": """❌ تحرك غير مسموح.""",
        "err_must_jump": """⚠️ الأكل إجباري!""",
        "err_chain_jump": """🔗 يمكنك القفز مجدداً!""",
        "err_king_must_jump": """👑 الملك يجب أن يأكل!""",
        "err_man_no_backward": """🚫 القطع العادية لا ترجع للخلف!""",
        "err_no_piece_here": """🔍 لا يوجد قطعة لك هنا.""",
        "err_already_in_game": """🎮 أنهِ اللعبة الحالية!""",
        "err_king_promoted_chain": """👑⚡ أصبحت ملكاً! استمر في الأكل!""",
        "timeout_winner": """⏲️ <b>انتهت اللعبة — فوز {winner}!</b>
{loser} نفد وقته.""",
        "timeout_loser": """⏲️ <b>Selesai — {winner} menang!</b>
{loser} kehabisan waktu.""",
        "draw_offer_sent": """🤝 تم إرسال عرض تعادل.""",
        "draw_already_offered": """ℹ️ العرض مرسل بالفعل.""",
        "draw_offer_recv": """🤝 <b>عرض تعادل!</b>
هل تقبل؟""",
        "draw_accept_btn": """✅ نعم""",
        "draw_reject_btn": """❌ لا""",
        "draw_accepted_white": """🤝 <b>تعادل!</b>""",
        "draw_accepted_black": """🤝 <b>تعادل!</b>""",
        "draw_rejected_by_you": """❌ تم الرفض.""",
        "draw_rejected_notif": """❌ تم الرفض.""",
        "no_opponent_yet": """⏳ بانتظار الخصم.""",
        "not_participant": """🚫 أنت لست لاعباً هنا!""",
        "surrender_winner": """🏳️ <b>انتهت اللعبة — فوز {winner}!</b>""",
        "surrender_loser": """🏳️ <b>انتهت اللعبة — فوز {winner}!</b>""",
        "game_over_hint": """

🔄 لعبة جديدة: /start""",
        "searching": """🔍 <b>بحث عن خصم…</b>""",
        "cancel_search_btn": """❌ إلغاء""",
        "search_cancelled": """✅ تم إلغاء البحث.""",
        "already_searching": """ℹ️ أنت تبحث بالفعل.""",
        "match_found_white": """🎮 <b>بدأت اللعبة!</b>

أنت: ⚪ الأبيض""",
        "match_found_black": """🎮 <b>بدأت اللعبة!</b>

أنت: ⚫ الأسود""",
        "bot_game_start": """🤖 <b>بدأت لعبة البوت!</b>""",
        "inline_title": """⚪⚫ لعبة داما!""",
        "inline_desc": """العب مع الأصدقاء""",
        "inline_no_lang_btn": """👉 اذهب للبوت""",
        "inline_no_lang_msg": """اختر لغة أولاً.""",
        "group_color_select_msg": """🎮 <b>لعبة جماعية</b>""",
        "group_select_lang_btn": """🌍 اللغة""",
        "group_lang_changed": """✅ تم تغيير اللغة.""",
        "group_waiting_color": """— بانتظار —""",
        "friend_invite_title": """🎮 داما — مع صديق""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>لعبة صديق</b>

اختر لونك!""",
        "friend_join_white_btn": """⚪ الأبيض""",
        "friend_join_black_btn": """⚫ الأسود""",
        "friend_color_taken": """⚠️ اللون مأخوذ.""",
        "friend_game_starting": """🎮 تبدأ اللعبة…""",
        "friend_you_white": """⚪ أنت الأبيض!""",
        "friend_you_black": """⚫ أنت الأسود!""",
        "friend_self_join": """⚠️ لا يمكنك اللعب ضد نفسك!""",
        "game_over_winner": """🏳️ <b>انتهت اللعبة!</b>""",
        "game_over_loser": """🏳️ <b>انتهت اللعبة!</b>""",
        "game_over_draw": """🤝 <b>تعادل!</b>""",
        "bot_game_over_winner": """🏳️ <b>انتهت اللعبة!</b>""",
        "bot_game_over_loser": """🏳️ <b>انتهت اللعبة!</b>""",
        "surrender_winner_bot": """🏳️ <b>انتهت اللعبة!</b>""",
        "surrender_loser_bot": """🏳️ <b>انتهت اللعبة!</b>""",
        "timeout_winner_bot": """⏲️ <b>انتهت اللعبة!</b>""",
        "timeout_loser_bot": """⏲️ <b>انتهت اللعبة!</b>""",
        "broadcast_no_perm": """🚫 المشرف فقط.""",
        "broadcast_no_reply": """⚠️ رد على رسالة.""",
        "broadcast_done": """✅ تم.""",
        "group_game_start": """🎮 <b>بدأت اللعبة!</b>""",
        "draw_is_your_offer": """ℹ️ تم الطلب.""",
        "inline_bot_group_note": """🤖 لعبة بوت.""",
    },
    "id": {
        "select_language": """🌍 <b>Pilih Bahasa / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ Bahasa Inggris dipilih!""",
        "start_text": """⛀⛂ <b>Selamat datang di Bot Checkers!</b>

🎯 Catur 8x8 klasik — lawan bot, online, atau teman!
🏆 Sistem rating ELO • ⚡ Langkah real-time • ⏲️ 60 detik per langkah

📖 Aturan lengkap: /help
👇 Pilih mode dari menu:""",
        "info": """⛀⛂ <b>Selamat datang di Bot Checkers!</b>

🎯 Catur 8x8 klasik — lawan bot, online, atau teman!
🏆 Sistem rating ELO • ⚡ Langkah real-time • ⏲️ 60 detik per langkah

📖 Aturan lengkap: /help
👇 Pilih mode dari menu:""",
        "btn_profile": """👤 Profil Saya""",
        "btn_bot": """🤖 Main lawan Bot""",
        "btn_online": """🌐 Main Online""",
        "btn_friend": """🤝 Main dengan Teman""",
        "btn_rating": """🏆 Papan Peringkat""",
        "btn_other_bots": """📢 Saluran Kami""",
        "btn_add_group": """➕ Tambah ke Grup""",
        "btn_change_lang": """🌍 Ganti Bahasa""",
        "btn_back": """🔙 Kembali""",
        "btn_surrender": """🏳️ Menyerah""",
        "btn_draw": """🤝 Seri""",
        "profile_text": """👤 <b>{name}</b>
🏅 Rating ELO: {elo}

📊 Total game: {total_games}
🏆 Menang: {wins}
💔 Kalah: {losses}
🤝 Seri: {draws}""",
        "help_text": """🎮 <b>Bot Saski — Panduan Lengkap</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Perintah:</b>
• /start — Mulai / kembali ke menu
• /saski — Menu game
• /my — Statistik
• /rating — Papan peringkat
• /language — Bahasa

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Aturan:</b>
• ⚪ Putih naik, ⚫ Hitam turun
• Bidak biasa: jalan maju — bisa MAKAN MUNDUR
• Sampai baris akhir → jadi raja (damka)
• 👑 Raja: jalan segala arah
• ⚡ Makan itu wajib
• 🔗 Makan beruntun diperbolehkan
• 👑➡⚡ Jadi raja dan bisa makan? Harus lanjut!
• ⏲️ 60 detik!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Mode:</b>
• 🤖 <b>Bot</b> — Latihan
• 🌐 <b>Online</b> — Cari lawan
• 🤝 <b>Teman</b> — Main bareng

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO:</b>
• Menang: rating naik   • Kalah: rating turun
• Game bot tidak pengaruhi ELO.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Menu Peringkat</b>

List mana yang mau dilihat?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 Menang""",
        "top_elo_title": """🏅 <b>TOP 20 — ELO Tertinggi</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — Paling Banyak Menang</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} menang
""",
        "turn_white": """Giliran: ⚪ <b>{name}</b>  ⏲️ {sec}detik""",
        "turn_black": """Giliran: ⚫ <b>{name}</b>  ⏲️ {sec}detik""",
        "board_header": """⛀⛂ <b>Catur</b> — {mode}

⚪ Putih: <b>{white}</b>
⚫ Hitam: <b>{black}</b>

""",
        "waiting_player": """menunggu…""",
        "bot_label": """Bot 🤖""",
        "saski_cmd_menu": """<b>Catur</b> — Pilih mode:""",
        "saski_cmd_bot_btn": """🤖 Main lawan Bot""",
        "saski_cmd_frnd_btn": """🤝 Main dengan Teman""",
        "saski_btn_bot": """🤖 Main lawan Bot""",
        "saski_btn_friend": """🤝 Main dengan Teman""",
        "saski_menu_text": """⛀⛂ <b>Catur — Pilih Mode</b>

🤖 <b>Bot</b> — Latihan
🤝 <b>Teman</b> — Main bareng""",
        "err_game_not_found": """⚠️ Game tidak ditemukan.""",
        "draw_bot_not_allowed": """🤖 Bot tidak mau seri.""",
        "friend_pick_color_title": """🎮 <b>Game Teman — Pilih Warna</b>""",
        "friend_pick_color_text": """🎮 <b>Game Teman</b>

Pilih warna Anda:

⚪ Putih — duluan
⚫ Hitam — kedua

⚪ Putih: {white}
⚫ Hitam: {black}""",
        "piece_selected": """✅ Bidak dipilih.""",
        "friend_lang_btn": """🌍 Pilih Bahasa""",
        "friend_game_over_shared": """🏁 <b>Game selesai.</b>
{result}""",
        "mode_bot": """Bot""",
        "mode_pvp": """Online""",
        "mode_friend": """Teman""",
        "err_not_your_turn": """⛔ Bukan giliranmu!""",
        "err_invalid_move": """❌ Langkah tidak sah.""",
        "err_must_jump": """⚠️ Harus makan!""",
        "err_chain_jump": """🔗 Makan beruntun!""",
        "err_king_must_jump": """👑 Raja wajib makan!""",
        "err_man_no_backward": """🚫 Bidak biasa tidak bisa mundur!""",
        "err_no_piece_here": """🔍 Tidak ada bidakmu.""",
        "err_already_in_game": """🎮 Selesaikan game dulu!""",
        "err_king_promoted_chain": """👑⚡ Jadi raja! Lanjutkan makan!""",
        "timeout_winner": """⏲️ <b>Selesai — {winner} menang!</b>
{loser} kehabisan waktu.""",
        "timeout_loser": """⏲️ <b>Žaidimas baigtas — laimėjo {winner}!</b>
{loser} pritrūko laiko.""",
        "draw_offer_sent": """🤝 Tawaran seri dikirim.""",
        "draw_already_offered": """ℹ️ Tawaran sudah dikirim.""",
        "draw_offer_recv": """🤝 <b>Tawaran seri!</b>
Terima?""",
        "draw_accept_btn": """✅ Ya""",
        "draw_reject_btn": """❌ Tidak""",
        "draw_accepted_white": """🤝 <b>Seri!</b>""",
        "draw_accepted_black": """🤝 <b>Seri!</b>""",
        "draw_rejected_by_you": """❌ Ditolak.""",
        "draw_rejected_notif": """❌ Ditolak.""",
        "no_opponent_yet": """⏳ Menunggu lawan.""",
        "not_participant": """🚫 Bukan peserta!""",
        "surrender_winner": """🏳️ <b>Selesai — {winner} menang!</b>""",
        "surrender_loser": """🏳️ <b>Selesai — {winner} menang!</b>""",
        "game_over_hint": """

🔄 Game baru: /start""",
        "searching": """🔍 <b>Mencari lawan…</b>""",
        "cancel_search_btn": """❌ Batal""",
        "search_cancelled": """✅ Pencarian batal.""",
        "already_searching": """ℹ️ Anda sedang mencari.""",
        "match_found_white": """🎮 <b>Game mulai!</b>

Anda: ⚪ Putih""",
        "match_found_black": """🎮 <b>Game mulai!</b>

Anda: ⚫ Hitam""",
        "bot_game_start": """🤖 <b>Game bot mulai!</b>""",
        "inline_title": """⚪⚫ Main Catur!""",
        "inline_desc": """Main bareng teman""",
        "inline_no_lang_btn": """👉 Ke bot""",
        "inline_no_lang_msg": """Pilih bahasa dulu.""",
        "group_color_select_msg": """🎮 <b>Game Grup</b>""",
        "group_select_lang_btn": """🌍 Bahasa""",
        "group_lang_changed": """✅ Bahasa diganti.""",
        "group_waiting_color": """— menunggu —""",
        "friend_invite_title": """🎮 Catur — Main bareng teman""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Game Teman</b>

Pilih warna!""",
        "friend_join_white_btn": """⚪ Putih""",
        "friend_join_black_btn": """⚫ Hitam""",
        "friend_color_taken": """⚠️ Warna itu diambil.""",
        "friend_game_starting": """🎮 Game mulai…""",
        "friend_you_white": """⚪ Anda Putih!""",
        "friend_you_black": """⚫ Anda Hitam!""",
        "friend_self_join": """⚠️ Jangan lawan diri sendiri!""",
        "game_over_winner": """🏳️ <b>Selesai!</b>""",
        "game_over_loser": """🏳️ <b>Selesai!</b>""",
        "game_over_draw": """🤝 <b>Seri!</b>""",
        "bot_game_over_winner": """🏳️ <b>Selesai!</b>""",
        "bot_game_over_loser": """🏳️ <b>Selesai!</b>""",
        "surrender_winner_bot": """🏳️ <b>Selesai!</b>""",
        "surrender_loser_bot": """🏳️ <b>Selesai!</b>""",
        "timeout_winner_bot": """⏲️ <b>Selesai!</b>""",
        "timeout_loser_bot": """⏲️ <b>Selesai!</b>""",
        "broadcast_no_perm": """🚫 Admin saja.""",
        "broadcast_no_reply": """⚠️ Balas pesan.""",
        "broadcast_done": """✅ Selesai.""",
        "group_game_start": """🎮 <b>Game mulai!</b>""",
        "draw_is_your_offer": """ℹ️ Sudah ditawarkan.""",
        "inline_bot_group_note": """🤖 Game bot.""",
    },
    "lt": {
        "select_language": """🌍 <b>Pasirinkite kalbą / Select Language / Выберите язык</b>""",
        "lang_selected": """✅ Anglų kalba nustatyta!""",
        "start_text": """⛀⛂ <b>Sveiki atvykę į Šaškių Botą!</b>

🎯 Klasikinė 8x8 šaškė — prieš botą, internete arba su draugu!
🏆 ELO reitingų sistema • ⚡ Ėjimai realiu laiku • ⏲️ 60 sek. ėjimui

📖 Visos taisyklės: /help
👇 Pasirinkite režimą iš meniu:""",
        "info": """⛀⛂ <b>Sveiki atvykę į Šaškių Botą!</b>

🎯 Klasikinė 8x8 šaškė — prieš botą, internete arba su draugu!
🏆 ELO reitingų sistema • ⚡ Ėjimai realiu laiku • ⏲️ 60 sek. ėjimui

📖 Visos taisyklės: /help
👇 Pasirinkite režimą iš meniu:""",
        "btn_profile": """👤 Mano profilis""",
        "btn_bot": """🤖 Žaisti prieš botą""",
        "btn_online": """🌐 Žaisti internetu""",
        "btn_friend": """🤝 Žaisti su draugu""",
        "btn_rating": """🏆 Lyderių sąrašas""",
        "btn_other_bots": """📢 Mūsų kanalas""",
        "btn_add_group": """➕ Pridėti į grupę""",
        "btn_change_lang": """🌍 Pakeisti kalbą""",
        "btn_back": """🔙 Atgal""",
        "btn_surrender": """🏳️ Pasiduoti""",
        "btn_draw": """🤝 Lygiosios""",
        "profile_text": """👤 <b>{name}</b>
🏅 ELO reitingas: {elo}

📊 Iš viso žaidimų: {total_games}
🏆 Pergalės: {wins}
💔 Pralaimėjimai: {losses}
🤝 Lygiosios: {draws}""",
        "help_text": """🎮 <b>„Saski Bot“ — Pilnas gidas</b>

━━━━━━━━━━━━━━━━━━━━
📌 <b>Komandos:</b>
• /start — Pradėti / grįžti į meniu
• /saski — Žaidimų meniu (veikia ir grupėse)
• /my — Statistika
• /rating — ELO ir pergalių lentelės
• /language — Keisti kalbą

━━━━━━━━━━━━━━━━━━━━
⛀⛂ <b>Taisyklės:</b>
• ⚪ Balti eina į viršų, ⚫ Juodi į apačią
• Paprasta šaškė: eina tik į priekį — bet GALI KIRSTI ATGAL
• Pasiekus galą → tampa damka
• 👑 Damka: eina į 4 puses, neribotas atstumas
• ⚡ Kirtimas yra PRIVALOMAS
• 🔗 Kirtimų grandinė: šokinėkite toliau
• 👑➡⚡ Vos tapote damka ir galite kirsti? Būtina tęsti!
• ⏲️ 60 sekundžių ėjimui — laikas baigėsi, pralaimėjote!

━━━━━━━━━━━━━━━━━━━━
🎯 <b>Režimai:</b>
• 🤖 <b>Prieš botą</b> — Treniruotė
• 🌐 <b>Internete</b> — Ieškokite varžovo
• 🤝 <b>Draugas</b> — /saski → Draugas → spalva

━━━━━━━━━━━━━━━━━━━━
🏆 <b>ELO sistema:</b>
• Pergalė: reitingas ↑   • Pralaimėjimas: reitingas ↓
• Žaidimai su botais reitingo nekeičia.

━━━━━━━━━━━━━━━━━━━━""",
        "rating_menu": """🏆 <b>Lyderių meniu</b>

Kurį sąrašą norite peržiūrėti?""",
        "btn_top_elo": """🥇 TOP 20 ELO""",
        "btn_top_wins": """⚔️ TOP 20 pergalių""",
        "top_elo_title": """🏅 <b>TOP 20 — AUKŠČIAUSIAS ELO</b>

""",
        "top_wins_title": """⚔️ <b>TOP 20 — DAUGIAUSIA PERGALIŲ</b>

""",
        "rating_row_elo": """{idx}. {name} — 🏆 {val} ELO
""",
        "rating_row_wins": """{idx}. {name} — 🏆 {val} pergalės
""",
        "turn_white": """Ėjimas: ⚪ <b>{name}</b>  ⏲️ {sec}s""",
        "turn_black": """Ėjimas: ⚫ <b>{name}</b>  ⏲️ {sec}s""",
        "board_header": """⛀⛂ <b>Šaškės</b> — {mode}

⚪ Balti: <b>{white}</b>
⚫ Juodi: <b>{black}</b>

""",
        "waiting_player": """laukia…""",
        "bot_label": """Botas 🤖""",
        "saski_cmd_menu": """<b>Šaškės</b> — Pasirinkite režimą:""",
        "saski_cmd_bot_btn": """🤖 Žaisti prieš botą""",
        "saski_cmd_frnd_btn": """🤝 Žaisti su draugu""",
        "saski_btn_bot": """🤖 Žaisti prieš botą""",
        "saski_btn_friend": """🤝 Žaisti su draugu""",
        "saski_menu_text": """⛀⛂ <b>Šaškės — Pasirinkite</b>

🤖 <b>Bota</b> — Treniruotė
🤝 <b>Draugas</b> — Spalva ir žaidimas""",
        "err_game_not_found": """⚠️ Žaidimas nerastas.""",
        "draw_bot_not_allowed": """🤖 Botas negali sutikti su lygiosiomis.""",
        "friend_pick_color_title": """🎮 <b>Draugo žaidimas — Spalva</b>""",
        "friend_pick_color_text": """🎮 <b>Draugo žaidimas</b>

Pasirinkite spalvą:

⚪ Balti — pirmas
⚫ Juodi — antras

⚪ Balti: {white}
⚫ Juodi: {black}""",
        "piece_selected": """✅ Šaškė pasirinkta.""",
        "friend_lang_btn": """🌍 Pasirinkite kalbą""",
        "friend_game_over_shared": """🏁 <b>Žaidimas baigtas.</b>
{result}""",
        "mode_bot": """Prieš botą""",
        "mode_pvp": """Internete""",
        "mode_friend": """Su draugu""",
        "err_not_your_turn": """⛔ Ne jūsų ėjimas!""",
        "err_invalid_move": """❌ Neleistinas ėjimas.""",
        "err_must_jump": """⚠️ Privaloma kirsti!""",
        "err_chain_jump": """🔗 Kirtimų grandinė!""",
        "err_king_must_jump": """👑 Damka privalo kirsti!""",
        "err_man_no_backward": """🚫 Paprasta šaškė atgal neina!""",
        "err_no_piece_here": """🔍 Nėra jūsų šaškės.""",
        "err_already_in_game": """🎮 Užbaikite žaidimą!""",
        "err_king_promoted_chain": """👑⚡ Tapote damka! Kriskite toliau!""",
        "timeout_winner": """⏲️ <b>Žaidimas baigtas — laimėjo {winner}!</b>
{loser} pritrūko laiko.""",
        "timeout_loser": """⏲️ <b>Žaidimas baigtas — laimėjo {winner}!</b>
Pritrūko laiko.""",
        "draw_offer_sent": """🤝 Lygiosios pasiūlytos.""",
        "draw_already_offered": """ℹ️ Jau pasiūlyta.""",
        "draw_offer_recv": """🤝 <b>Siūlyti lygiąsias?</b>""",
        "draw_accept_btn": """✅ Taip""",
        "draw_reject_btn": """❌ Ne""",
        "draw_accepted_white": """🤝 <b>Lygiosios!</b>""",
        "draw_accepted_black": """🤝 <b>Lygiosios!</b>""",
        "draw_rejected_by_you": """❌ Atmesta.""",
        "draw_rejected_notif": """❌ Atmesta.""",
        "no_opponent_yet": """⏳ Laukiamas žaidėjas.""",
        "not_participant": """🚫 Ne jūsų žaidimas!""",
        "surrender_winner": """🏳️ <b>Laimėjo {winner}!</b>""",
        "surrender_loser": """🏳️ <b>Laimėjo {winner}!</b>""",
        "game_over_hint": """

🔄 Naujas žaidimas: /start""",
        "searching": """🔍 <b>Ieškoma varžovo…</b>""",
        "cancel_search_btn": """❌ Atšaukti""",
        "search_cancelled": """✅ Atšaukta.""",
        "already_searching": """ℹ️ Jau ieškote.""",
        "match_found_white": """🎮 <b>Žaidimas prasideda!</b>

Jūs: ⚪ Balti""",
        "match_found_black": """🎮 <b>Žaidimas prasideda!</b>

Jūs: ⚫ Juodi""",
        "bot_game_start": """🤖 <b>Žaidimas prasidėjo!</b>""",
        "inline_title": """⚪⚫ Šaškės!""",
        "inline_desc": """Žaisk su draugu""",
        "inline_no_lang_btn": """👉 Eiti į botą""",
        "inline_no_lang_msg": """Pasirinkite kalbą.""",
        "group_color_select_msg": """🎮 <b>Žaidimas grupėje</b>""",
        "group_select_lang_btn": """🌍 Kalba""",
        "group_lang_changed": """✅ Kalba pakeista.""",
        "group_waiting_color": """— laukia —""",
        "friend_invite_title": """🎮 Šaškės — Žaisti su draugu""",
        "friend_invite_desc_az": """Dəvəti at, rəng seç, oyna! (AZ)""",
        "friend_invite_desc_ru": """Поделись, выбери цвет, играй! (RU)""",
        "friend_invite_desc_en": """Share the game, pick colour, play! (EN)""",
        "friend_waiting_msg": """🎮 <b>Draugo žaidimas</b>

Pasirinkite spalvą!""",
        "friend_join_white_btn": """⚪ Balti""",
        "friend_join_black_btn": """⚫ Juodi""",
        "friend_color_taken": """⚠️ Spalva užimta.""",
        "friend_game_starting": """🎮 Žaidimas prasideda…""",
        "friend_you_white": """⚪ Jūs balti!""",
        "friend_you_black": """⚫ Jūs juodi!""",
        "friend_self_join": """⚠️ Negalima su savimi!""",
        "game_over_winner": """🏳️ <b>Žaidimas baigtas!</b>""",
        "game_over_loser": """🏳️ <b>Žaidimas baigtas!</b>""",
        "game_over_draw": """🤝 <b>Lygiosios!</b>""",
        "bot_game_over_winner": """🏳️ <b>Žaidimas baigtas!</b>""",
        "bot_game_over_loser": """🏳️ <b>Žaidimas baigtas!</b>""",
        "surrender_winner_bot": """🏳️ <b>Žaidimas baigtas!</b>""",
        "surrender_loser_bot": """🏳️ <b>Žaidimas baigtas!</b>""",
        "timeout_winner_bot": """⏲️ <b>Žaidimas baigtas!</b>""",
        "timeout_loser_bot": """⏲️ <b>Žaidimas baigtas!</b>""",
        "broadcast_no_perm": """🚫 Tik adminams.""",
        "broadcast_no_reply": """⚠️ Atsakykite į žinutę.""",
        "broadcast_done": """✅ Atlikta.""",
        "group_game_start": """🎮 <b>Žaidimas prasidėjo!</b>""",
        "draw_is_your_offer": """ℹ️ Jau pasiūlyta.""",
        "inline_bot_group_note": """🤖 Žaidimas su botu.""",
    },
}

def t(lang_code: str, key: str, **kwargs) -> str:
    if lang_code not in LOCALES:
        lang_code = "az"
    template = LOCALES[lang_code].get(key, LOCALES["az"].get(key, key))
    if kwargs:
        return template.format(**kwargs)
    return template
