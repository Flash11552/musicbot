# database.py - SQLite verilənlər bazası idarəetməsi

import sqlite3
import json
import os
import math
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saski.db")

ELO_K = 32
ELO_START = 1000


# ---------------------------------------------------------------------------
# Baglanti
# ---------------------------------------------------------------------------

def _conn():
    # timeout=30: paralel qrup oyunlarında kilidlənmə gözləməsi
    # WAL: eyni anda bir yazma + çox oxuma (qrup donmalarının kök səbəbini həll edir)
    c = sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    return c


# ---------------------------------------------------------------------------
# Verilənlər bazasinin yaradilmasi
# ---------------------------------------------------------------------------

def init_db():
    with _conn() as con:
        con.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                user_id     INTEGER PRIMARY KEY,
                username    TEXT    DEFAULT '',
                lang        TEXT,
                rating      INTEGER DEFAULT 1000,
                wins        INTEGER DEFAULT 0,
                losses      INTEGER DEFAULT 0,
                draws       INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS games (
                game_id           TEXT PRIMARY KEY,
                player_white      INTEGER,
                player_black      INTEGER,
                board             TEXT    NOT NULL,
                turn              TEXT    DEFAULT 'white',
                selected_cell     TEXT,
                last_token_type   TEXT,
                game_type         TEXT,
                error_msg         TEXT,
                err_recipient     INTEGER,
                draw_offered_by   INTEGER,
                last_move_time    TEXT,
                white_chat_id     INTEGER,
                white_msg_id      INTEGER,
                black_chat_id     INTEGER,
                black_msg_id      INTEGER,
                inline_msg_id     TEXT,
                shared_chat_id    INTEGER,
                shared_msg_id     INTEGER
            );

            CREATE TABLE IF NOT EXISTS queue (
                user_id   INTEGER PRIMARY KEY,
                joined_at TEXT
            );

            CREATE TABLE IF NOT EXISTS chats (
                chat_id    INTEGER PRIMARY KEY,
                chat_type  TEXT    DEFAULT 'private',
                title      TEXT    DEFAULT '',
                joined_at  TEXT
            );
        """)
        # Köhnə bazalarda çatışmayan sütunları əlavə et
        _safe_add_column(con, "users", "wins",          "INTEGER DEFAULT 0")
        _safe_add_column(con, "users", "username",      "TEXT DEFAULT ''")
        _safe_add_column(con, "games", "game_lang",     "TEXT")
        _safe_add_column(con, "games", "shared_chat_id","INTEGER")
        _safe_add_column(con, "games", "shared_msg_id", "INTEGER")


def _safe_add_column(con, table, column, definition):
    existing = {row[1] for row in con.execute(f"PRAGMA table_info({table})")}
    if column not in existing:
        con.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


# ---------------------------------------------------------------------------
# İstifadeci emeliyyatlari
# ---------------------------------------------------------------------------

def get_user(user_id: int) -> dict:
    """İstifadecini qaytarir; yoxdursa yaradir."""
    with _conn() as con:
        row = con.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()
        if row is None:
            con.execute(
                "INSERT INTO users (user_id, username, lang, rating) VALUES (?, '', NULL, ?)",
                (user_id, ELO_START)
            )
            return {
                "user_id": user_id, "username": "",
                "lang": None, "rating": ELO_START,
                "wins": 0, "losses": 0, "draws": 0
            }
        return dict(row)


def set_lang(user_id: int, lang: str):
    get_user(user_id)
    with _conn() as con:
        con.execute(
            "UPDATE users SET lang = ? WHERE user_id = ?",
            (lang, user_id)
        )


def update_username(user_id: int, username: str):
    """İstifadecinin adini DB-ye qeyd edir."""
    get_user(user_id)
    with _conn() as con:
        con.execute(
            "UPDATE users SET username = ? WHERE user_id = ?",
            (username or "", user_id)
        )


def get_username(user_id: int) -> str:
    """DB-den istifadeci adini qaytarir."""
    if user_id == 0:
        return "Bot"
    u = get_user(user_id)
    return u.get("username") or str(user_id)


def get_active_game(user_id: int):
    """İstifadecinin aktiv oyununu qaytarir (yoxdursa None)."""
    with _conn() as con:
        row = con.execute(
            "SELECT game_id FROM games WHERE player_white = ? OR player_black = ?",
            (user_id, user_id)
        ).fetchone()
    return row["game_id"] if row else None


# ---------------------------------------------------------------------------
# Oyun emeliyyatlari
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def seconds_since(iso_str: str) -> float:
    """Verilmis ISO zamandan indiyə qeder kecen saniyeler."""
    try:
        t = datetime.fromisoformat(iso_str)
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - t).total_seconds()
    except Exception:
        return 0.0


def create_game(game_id: str, player_white: int, board: list,
                game_type: str, player_black: int = None,
                game_lang: str = None):
    with _conn() as con:
        con.execute("""
            INSERT OR REPLACE INTO games
                (game_id, player_white, player_black, board, turn,
                 selected_cell, last_token_type, game_type,
                 error_msg, err_recipient, draw_offered_by,
                 last_move_time, game_lang)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            game_id, player_white, player_black,
            json.dumps(board), "white",
            None, None, game_type,
            None, None, None, _now_iso(),
            game_lang
        ))


def get_game(game_id: str):
    with _conn() as con:
        row = con.execute(
            "SELECT * FROM games WHERE game_id = ?", (game_id,)
        ).fetchone()
    if row is None:
        return None
    d = dict(row)
    d["board"] = json.loads(d["board"])
    d["selected_cell"] = json.loads(d["selected_cell"]) if d["selected_cell"] else None
    return d


def update_game(game_id: str, board: list, turn: str, selected_cell,
                last_token_type: str = None,
                error_msg: str = None, err_recipient: int = None,
                player_black: int = None,
                player_white: int = None,
                draw_offered_by: int = None,
                white_chat_id: int = None, white_msg_id: int = None,
                black_chat_id: int = None, black_msg_id: int = None,
                inline_msg_id: str = None,
                game_lang: str = None,
                update_move_time: bool = True,
                clear_player_white: bool = False,
                clear_player_black: bool = False):
    """Oyun veziyyetini yenileyir. None oturulen saheler deyismir."""
    with _conn() as con:
        row = con.execute(
            "SELECT * FROM games WHERE game_id = ?", (game_id,)
        ).fetchone()
        if row is None:
            return
        ex = dict(row)

        pw_val = None if clear_player_white else (player_white if player_white is not None else ex["player_white"])
        pb_val = None if clear_player_black else (player_black if player_black is not None else ex["player_black"])

        con.execute("""
            UPDATE games SET
                board           = ?,
                turn            = ?,
                selected_cell   = ?,
                last_token_type = ?,
                error_msg       = ?,
                err_recipient   = ?,
                draw_offered_by = ?,
                last_move_time  = ?,
                player_white    = ?,
                player_black    = ?,
                white_chat_id   = ?,
                white_msg_id    = ?,
                black_chat_id   = ?,
                black_msg_id    = ?,
                inline_msg_id   = ?,
                game_lang       = ?
            WHERE game_id = ?
        """, (
            json.dumps(board),
            turn,
            json.dumps(selected_cell) if selected_cell is not None else None,
            last_token_type if last_token_type is not None else ex["last_token_type"],
            error_msg,
            err_recipient,
            draw_offered_by if draw_offered_by is not None else ex["draw_offered_by"],
            _now_iso() if update_move_time else ex["last_move_time"],
            pw_val,
            pb_val,
            white_chat_id   if white_chat_id   is not None else ex["white_chat_id"],
            white_msg_id    if white_msg_id    is not None else ex["white_msg_id"],
            black_chat_id   if black_chat_id   is not None else ex["black_chat_id"],
            black_msg_id    if black_msg_id    is not None else ex["black_msg_id"],
            inline_msg_id   if inline_msg_id   is not None else ex["inline_msg_id"],
            game_lang       if game_lang       is not None else ex.get("game_lang"),
            game_id
        ))


def update_game_msg_ids(game_id: str,
                        white_chat_id: int = None, white_msg_id: int = None,
                        black_chat_id: int = None, black_msg_id: int = None,
                        inline_msg_id: str = None,
                        shared_chat_id: int = None, shared_msg_id: int = None):
    """Yalniz mesaj ID-lerini yenileyir."""
    with _conn() as con:
        row = con.execute(
            "SELECT * FROM games WHERE game_id = ?", (game_id,)
        ).fetchone()
        if row is None:
            return
        ex = dict(row)
        con.execute("""
            UPDATE games SET
                white_chat_id  = ?,
                white_msg_id   = ?,
                black_chat_id  = ?,
                black_msg_id   = ?,
                inline_msg_id  = ?,
                shared_chat_id = ?,
                shared_msg_id  = ?
            WHERE game_id = ?
        """, (
            white_chat_id  if white_chat_id  is not None else ex["white_chat_id"],
            white_msg_id   if white_msg_id   is not None else ex["white_msg_id"],
            black_chat_id  if black_chat_id  is not None else ex["black_chat_id"],
            black_msg_id   if black_msg_id   is not None else ex["black_msg_id"],
            inline_msg_id  if inline_msg_id  is not None else ex["inline_msg_id"],
            shared_chat_id if shared_chat_id is not None else ex.get("shared_chat_id"),
            shared_msg_id  if shared_msg_id  is not None else ex.get("shared_msg_id"),
            game_id
        ))


def delete_game(game_id: str):
    with _conn() as con:
        con.execute("DELETE FROM games WHERE game_id = ?", (game_id,))


# ---------------------------------------------------------------------------
# Esleme novbesi
# ---------------------------------------------------------------------------

def add_to_queue(user_id: int) -> bool:
    """Novbeye elave edir. Artiq varsa False qaytarir."""
    with _conn() as con:
        ex = con.execute(
            "SELECT 1 FROM queue WHERE user_id = ?", (user_id,)
        ).fetchone()
        if ex:
            return False
        con.execute(
            "INSERT INTO queue (user_id, joined_at) VALUES (?, ?)",
            (user_id, _now_iso())
        )
    return True


def get_queue_opponent(user_id: int):
    """Novbede baska oyuncu varsa onu silir ve ID-ni qaytarir."""
    with _conn() as con:
        row = con.execute(
            "SELECT user_id FROM queue WHERE user_id != ? ORDER BY joined_at LIMIT 1",
            (user_id,)
        ).fetchone()
        if row is None:
            return None
        opp = row["user_id"]
        con.execute("DELETE FROM queue WHERE user_id IN (?, ?)", (user_id, opp))
    return opp


def leave_queue(user_id: int):
    with _conn() as con:
        con.execute("DELETE FROM queue WHERE user_id = ?", (user_id,))


# ---------------------------------------------------------------------------
# ELO statistikasi
# ---------------------------------------------------------------------------

def _elo_delta(r_a: int, r_b: int, score_a: float) -> int:
    e_a = 1.0 / (1.0 + math.pow(10, (r_b - r_a) / 400.0))
    return round(ELO_K * (score_a - e_a))


def update_stats(winner_id: int, loser_id: int, is_draw: bool):
    """Qalibiyyat/meglubiyet/hec-hece statistikasini ve ELO-nu yenileyir.
    Bot (id=0) ucun statistika yenilenmez."""
    with _conn() as con:
        w_row = con.execute(
            "SELECT rating FROM users WHERE user_id = ?", (winner_id,)
        ).fetchone() if winner_id != 0 else None
        l_row = con.execute(
            "SELECT rating FROM users WHERE user_id = ?", (loser_id,)
        ).fetchone() if loser_id != 0 else None

        r_w = w_row["rating"] if w_row else ELO_START
        r_l = l_row["rating"] if l_row else ELO_START

        if is_draw:
            dw = _elo_delta(r_w, r_l, 0.5)
            dl = _elo_delta(r_l, r_w, 0.5)
            if winner_id != 0:
                con.execute(
                    "UPDATE users SET rating = MAX(100, rating + ?), draws = draws + 1 WHERE user_id = ?",
                    (dw, winner_id)
                )
            if loser_id != 0:
                con.execute(
                    "UPDATE users SET rating = MAX(100, rating + ?), draws = draws + 1 WHERE user_id = ?",
                    (dl, loser_id)
                )
        else:
            dw = _elo_delta(r_w, r_l, 1.0)
            dl = _elo_delta(r_l, r_w, 0.0)
            if winner_id != 0:
                con.execute(
                    "UPDATE users SET rating = MAX(100, rating + ?), wins = wins + 1 WHERE user_id = ?",
                    (dw, winner_id)
                )
            if loser_id != 0:
                con.execute(
                    "UPDATE users SET rating = MAX(100, rating + ?), losses = losses + 1 WHERE user_id = ?",
                    (dl, loser_id)
                )


# ---------------------------------------------------------------------------
# Reytinq siyahilari
# ---------------------------------------------------------------------------

def get_top_20_elo():
    with _conn() as con:
        rows = con.execute(
            "SELECT user_id, username, rating FROM users WHERE user_id != 0 ORDER BY rating DESC LIMIT 20"
        ).fetchall()
    return [(r["user_id"], r["username"] or str(r["user_id"]), r["rating"]) for r in rows]


def get_top_20_wins():
    with _conn() as con:
        rows = con.execute(
            "SELECT user_id, username, wins FROM users WHERE user_id != 0 ORDER BY wins DESC LIMIT 20"
        ).fetchall()
    return [(r["user_id"], r["username"] or str(r["user_id"]), r["wins"]) for r in rows]


# ---------------------------------------------------------------------------
# Yayim (Broadcast) xidmeti
# ---------------------------------------------------------------------------

def register_chat(chat_id: int, chat_type: str, title: str = ""):
    """İstifadəçi və ya qrup yaddaşa alınır."""
    with _conn() as con:
        con.execute("""
            INSERT INTO chats (chat_id, chat_type, title, joined_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(chat_id) DO UPDATE SET chat_type=excluded.chat_type,
                                                title=excluded.title
        """, (chat_id, chat_type, title or "", _now_iso()))


def get_all_chats() -> list:
    """Bütün qeydə alınmış chat_id-ləri qaytarır."""
    with _conn() as con:
        rows = con.execute("SELECT chat_id FROM chats").fetchall()
    return [r["chat_id"] for r in rows]


# ---------------------------------------------------------------------------
# ELO deltası (xarici hesablama üçün)
# ---------------------------------------------------------------------------

def compute_elo_deltas(winner_id: int, loser_id: int, is_draw: bool):
    """ELO dəyişikliklərini hesablayıb (delta_w, delta_l) qaytarır, DB-ni dəyişmir."""
    with _conn() as con:
        w_row = con.execute(
            "SELECT rating FROM users WHERE user_id = ?", (winner_id,)
        ).fetchone() if winner_id and winner_id != 0 else None
        l_row = con.execute(
            "SELECT rating FROM users WHERE user_id = ?", (loser_id,)
        ).fetchone() if loser_id and loser_id != 0 else None
    r_w = w_row["rating"] if w_row else ELO_START
    r_l = l_row["rating"] if l_row else ELO_START
    if is_draw:
        return _elo_delta(r_w, r_l, 0.5), _elo_delta(r_l, r_w, 0.5)
    return _elo_delta(r_w, r_l, 1.0), _elo_delta(r_l, r_w, 0.0)
