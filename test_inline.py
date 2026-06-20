#!/usr/bin/env python3
"""
test_inline.py — Inline query diaqnostika skripti

İSTİFADƏ:
  1. Botu DAYANDIRIN (main.py çalışırsa Ctrl+C)
  2. Bu skripti işə salın:
       python test_inline.py
  3. Başqa bir cihazda / Telegram-da:
       @SaskiGameBot yazın (boşluq da qoyun)
  4. Bu skriptin terminalında nə çıxdığına baxın

Nə görürsünüz?
  ✅ "INLINE_QUERY alındı!" — bot API-dan inline query gəlir, problem main.py-dadır
  ❌ Heç nə çıxmır   — Telegram bot-a inline query göndərmir (BotFather/API məsələsi)
"""

import asyncio
import os
import sys
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("XƏTA: .env faylında BOT_TOKEN tapılmadı!")
    sys.exit(1)

ALLOWED = ["message", "callback_query", "inline_query", "chosen_inline_result"]


async def run():
    bot = Bot(token=BOT_TOKEN)

    # 1) Webhook sil
    await bot.delete_webhook(drop_pending_updates=True)
    print("[1/3] Webhook silindi.")

    # 2) Telegram allowed_updates-i sıfırla
    await bot.get_updates(timeout=0, allowed_updates=ALLOWED)
    print(f"[2/3] Telegram abunəsi: {ALLOWED}")
    print()
    print("=" * 55)
    print("  İNDİ Telegram-da @SaskiGameBot yazın (boşluq əlavə edin)")
    print("  Inline query göndərin — bu terminala yansıyacaq")
    print("=" * 55)
    print()

    # 3) getUpdates loop — raw API ilə, aiogram dispatcher olmadan
    offset = None
    timeout_sec = 30
    check_count = 0

    while check_count < 10:   # 10 × 30s = 5 dəqiqə
        check_count += 1
        print(f"[Poll {check_count}/10] gözlənilir ({timeout_sec}s)...")
        updates = await bot.get_updates(
            offset=offset,
            timeout=timeout_sec,
            allowed_updates=ALLOWED
        )

        if not updates:
            print("   — bu dövrdə update yoxdur.")
            continue

        for upd in updates:
            offset = upd.update_id + 1
            print(f"\n  ► Update ID: {upd.update_id}")

            if upd.inline_query:
                iq = upd.inline_query
                print(f"  ✅ INLINE_QUERY ALINDI!")
                print(f"     user_id : {iq.from_user.id}")
                print(f"     query   : {repr(iq.query)}")
                print(f"\n  KOD İŞLƏYİR — problem main.py-dadır.")
                print(f"  main.py-ni yeni fayldan yükləyin, botu yenidən başladın.")

                # Test cavabı göndər
                from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
                await bot.answer_inline_query(
                    iq.id,
                    results=[
                        InlineQueryResultArticle(
                            id="test",
                            title="✅ TEST — İşləyir!",
                            description="Inline sual doğru alındı",
                            input_message_content=InputTextMessageContent(message_text="✅ Saski bot inline test uğurludur!")
                        )
                    ],
                    cache_time=0
                )
                print("  Test kartı göndərildi!")
                await bot.session.close()
                return

            elif upd.message:
                print(f"     message: {upd.message.text!r} (from {upd.message.from_user.id})")
            elif upd.callback_query:
                print(f"     callback_query: {upd.callback_query.data!r}")
            else:
                print(f"     digər update tipi")

    print("\n[NƏTICƏ] 5 dəqiqə ərzində inline_query gəlmədi.")
    print("         BotFather-da @SaskiGameBot → Bot Settings → Inline Mode yoxlayın.")
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(run())
