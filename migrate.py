# migrate.py — Köhnə saski.db bazasını yeni sxemə yüksəlt
# Bir dəfə işlət: python migrate.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saski.db")

# games cədvəlinə əlavə olunacaq sütunlar: (ad, tip)
MISSING_COLUMNS = [
    ("error_msg",       "TEXT"),
    ("err_recipient",   "INTEGER"),
    ("draw_offered_by", "INTEGER"),
    ("last_move_time",  "TEXT"),
    ("white_chat_id",   "INTEGER"),
    ("white_msg_id",    "INTEGER"),
    ("black_chat_id",   "INTEGER"),
    ("black_msg_id",    "INTEGER"),
    ("inline_msg_id",   "TEXT"),
    ("last_token_type", "TEXT"),
]

def migrate():
    con = sqlite3.connect(DB_PATH)

    # --- games cədvəli sütunları ---
    existing = {row[1] for row in con.execute("PRAGMA table_info(games)")}
    print(f"📋 games sütunları: {existing}")

    added = []
    for col_name, col_type in MISSING_COLUMNS:
        if col_name not in existing:
            try:
                con.execute(f"ALTER TABLE games ADD COLUMN {col_name} {col_type}")
                added.append(col_name)
                print(f"  ✅ Sütun əlavə edildi: {col_name}")
            except sqlite3.OperationalError as e:
                print(f"  ⚠️  {col_name} — xəta: {e}")
        else:
            print(f"  ✔  {col_name} artıq mövcuddur, atlıldı.")

    # --- chats cədvəli yoxla / yarat ---
    tables = {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if "chats" not in tables:
        con.execute("""
            CREATE TABLE chats (
                chat_id   INTEGER PRIMARY KEY,
                chat_type TEXT    DEFAULT 'private',
                title     TEXT    DEFAULT '',
                joined_at TEXT
            )
        """)
        print("  ✅ chats cədvəli yaradıldı.")
    else:
        print("  ✔  chats cədvəli artıq mövcuddur.")

    con.commit()
    con.close()

    if added:
        print(f"\n🎉 Miqrasiya tamamlandı! Əlavə edilən sütunlar: {added}")
    else:
        print("\n✅ Baza artıq yeni sxemdədir, heç nə dəyişmədi.")

if __name__ == "__main__":
    migrate()
