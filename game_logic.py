# game_logic.py - Dama oyun mentiqi
#
# Qaydalar:
# - Adi das: ireli gedir, amma GERIYE YEYEBILIR (atlama)
# - Dama (king): 4 istiqamete, ISTENEN MESAFEYE gede bilir (ucan dama)
# - Mecburi yeme: atlama imkani varsa mutleq atlamaq lazimdir
# - Ardisil yeme: bir gedisde bir nece das art arda yeyile biler
# - Dama uzaq daşı yeyir: diagonal üzrə istənilən məsafədən

WHITE_MAN  = "\u26aa"   # ⚪
WHITE_KING = "\u25fb\ufe0f"  # ◻️
BLACK_MAN  = "\u26ab"   # ⚫
BLACK_KING = "\u25fc\ufe0f"  # ◼️

WHITE_PIECES  = {WHITE_MAN, WHITE_KING}
BLACK_PIECES  = {BLACK_MAN, BLACK_KING}
ALL_PIECES    = WHITE_PIECES | BLACK_PIECES
LIGHT_SQUARE  = " "
EMPTY_DARK    = "."
SELECTED_MARK = "\U0001f4cd"  # 📍


# ---------------------------------------------------------------------------
# Lovhe yaratma
# ---------------------------------------------------------------------------

def create_initial_board():
    board = []
    for r in range(8):
        row = []
        for c in range(8):
            if (r + c) % 2 == 0:
                row.append(LIGHT_SQUARE)
            elif r < 3:
                row.append(BLACK_MAN)
            elif r > 4:
                row.append(WHITE_MAN)
            else:
                row.append(EMPTY_DARK)
        board.append(row)
    return board


# ---------------------------------------------------------------------------
# Komekci funksiyalar
# ---------------------------------------------------------------------------

def _is_valid(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def _pieces_of(color):
    return WHITE_PIECES if color == "white" else BLACK_PIECES


def _opponent_pieces_of(color):
    return BLACK_PIECES if color == "white" else WHITE_PIECES


def _king_of(color):
    return WHITE_KING if color == "white" else BLACK_KING


def _man_of(color):
    return WHITE_MAN if color == "white" else BLACK_MAN


def _promotion_row(color):
    return 0 if color == "white" else 7


def _forward_directions(color):
    """Adi dasin ireli hereketinin istiquemleri."""
    return [(-1, -1), (-1, 1)] if color == "white" else [(1, -1), (1, 1)]


def _all_directions():
    return [(-1, -1), (-1, 1), (1, -1), (1, 1)]


# ---------------------------------------------------------------------------
# Bir dasin mumkun atlamalarini tap
# ---------------------------------------------------------------------------

def get_piece_jumps(board, pos, color):
    """
    Verilmis movqedeki dasin mumkun atlamalarini qaytarir.
    Adi das: 4 istiqametde yeyebilir (o cumleden geriye)
    Dama: 4 istiqametde, istenen mesafedeki raqib daşi yeyebilir
    Netice: list of (from_pos, to_pos, captured_pos)
    """
    r, c = pos
    token = board[r][c]
    if token not in _pieces_of(color):
        return []

    is_king = token == _king_of(color)
    opponent = _opponent_pieces_of(color)
    jumps = []

    if is_king:
        # Ucan dama: her istiqametde raqib dasi axtar
        for dr, dc in _all_directions():
            dist = 1
            while True:
                mr, mc = r + dr * dist, c + dc * dist
                if not _is_valid(mr, mc):
                    break
                cell = board[mr][mc]
                if cell in _pieces_of(color):
                    break  # oz dasi - bu istiqameti kes
                if cell in opponent:
                    # Arxasinda bos xana varmı?
                    lr, lc = r + dr * (dist + 1), c + dc * (dist + 1)
                    if _is_valid(lr, lc) and board[lr][lc] == EMPTY_DARK:
                        jumps.append(((r, c), (lr, lc), (mr, mc)))
                    break  # raqib dasindan sonra devam etme (tek atlama)
                # Bos xana - dama keche biler, amma bu hissede atlama yoxdur
                dist += 1
    else:
        # Adi das: 4 istiqametde atlama (geriye de yeyebilir)
        for dr, dc in _all_directions():
            mr, mc = r + dr, c + dc
            lr, lc = r + 2 * dr, c + 2 * dc
            if (_is_valid(lr, lc)
                    and board[mr][mc] in opponent
                    and board[lr][lc] == EMPTY_DARK):
                jumps.append(((r, c), (lr, lc), (mr, mc)))

    return jumps


# ---------------------------------------------------------------------------
# Butun mecburi atlamalar
# ---------------------------------------------------------------------------

def get_all_mandatory_jumps(board, color):
    pieces = _pieces_of(color)
    jumps = []
    for r in range(8):
        for c in range(8):
            if board[r][c] in pieces:
                jumps.extend(get_piece_jumps(board, (r, c), color))
    return jumps


# ---------------------------------------------------------------------------
# Butun mumkun adi hereketler (atlama yox)
# ---------------------------------------------------------------------------

def get_all_possible_moves(board, color):
    pieces = _pieces_of(color)
    moves = []
    for r in range(8):
        for c in range(8):
            token = board[r][c]
            if token not in pieces:
                continue
            is_king = token == _king_of(color)
            if is_king:
                # Dama: 4 istiqametde istenen mesafeye
                for dr, dc in _all_directions():
                    dist = 1
                    while True:
                        nr, nc = r + dr * dist, c + dc * dist
                        if not _is_valid(nr, nc):
                            break
                        if board[nr][nc] == EMPTY_DARK:
                            moves.append(((r, c), (nr, nc)))
                            dist += 1
                        else:
                            break
            else:
                # Adi das: yalniz ireli
                for dr, dc in _forward_directions(color):
                    nr, nc = r + dr, c + dc
                    if _is_valid(nr, nc) and board[nr][nc] == EMPTY_DARK:
                        moves.append(((r, c), (nr, nc)))
    return moves


# ---------------------------------------------------------------------------
# Hereketi yoxla ve icra et
# ---------------------------------------------------------------------------

def validate_and_execute_move(board, from_pos, to_pos, color):
    """
    Hereketi yoxlayir ve icra edir.
    Qaytarir:
      {"status": "error",  "reason": "<lokalizasiya_acari>"}
      {"status": "ok",     "board": <yeni_lovhe>, "switch_turn": bool,
       "captured": bool,   "chain_possible": bool}
    """
    r1, c1 = from_pos
    r2, c2 = to_pos

    # Secim isamesi varsa gercek tokeni berpea et
    token = board[r1][c1]
    if token == SELECTED_MARK:
        return {"status": "error", "reason": "err_no_piece_here"}

    if token not in _pieces_of(color):
        return {"status": "error", "reason": "err_no_piece_here"}
    if not _is_valid(r2, c2) or board[r2][c2] != EMPTY_DARK:
        return {"status": "error", "reason": "err_invalid_move"}

    dr = r2 - r1
    dc = c2 - c1
    is_king = token == _king_of(color)

    mandatory_jumps = get_all_mandatory_jumps(board, color)

    # --- ATLAMA GEDİŞİ yoxla ---
    # Verilmis (from, to) cütü mecburi atlamalar arasindan var mi?
    piece_jumps = get_piece_jumps(board, from_pos, color)
    jump_targets = {j[1]: j[2] for j in piece_jumps}  # to_pos -> captured_pos

    if (r2, c2) in jump_targets:
        # Bu bir atlama gedisidir
        if mandatory_jumps and (from_pos, (r2, c2)) not in [(j[0], j[1]) for j in mandatory_jumps]:
            # Atlama movcuddur amma bu das ile degil - mecburi das ile yemek lazimdir
            return {"status": "error", "reason": "err_must_jump"}

        cap_r, cap_c = jump_targets[(r2, c2)]

        new_board = [row[:] for row in board]
        new_board[r1][c1] = EMPTY_DARK
        new_board[cap_r][cap_c] = EMPTY_DARK

        # Dama olmasi yoxlanir
        if r2 == _promotion_row(color):
            new_board[r2][c2] = _king_of(color)
            # YENİ QAYDA: Dama olan kimi yeyə biləcəyi daş varsa zəncir DAVAM EDİR
            king_chain = get_piece_jumps(new_board, (r2, c2), color)
            if king_chain:
                return {
                    "status": "ok",
                    "board": new_board,
                    "switch_turn": False,
                    "captured": True,
                    "chain_possible": True,
                    "just_promoted": True
                }
            return {
                "status": "ok",
                "board": new_board,
                "switch_turn": True,
                "captured": True,
                "chain_possible": False
            }
        else:
            new_board[r2][c2] = token

        # Zencir atlama mumkundurmu?
        chain = get_piece_jumps(new_board, (r2, c2), color)
        switch_turn = len(chain) == 0

        return {
            "status": "ok",
            "board": new_board,
            "switch_turn": switch_turn,
            "captured": True,
            "chain_possible": not switch_turn
        }

    # --- ADİ GEDİŞ yoxla ---
    # Mecburi atlama varsa adi gedis qadagandir
    if mandatory_jumps:
        return {"status": "error", "reason": "err_must_jump"}

    if is_king:
        # Dama: eyni diaqonal, ard-arda bos xanalar
        if abs(dr) != abs(dc) or dr == 0:
            return {"status": "error", "reason": "err_invalid_move"}
        step_r = 1 if dr > 0 else -1
        step_c = 1 if dc > 0 else -1
        steps  = abs(dr)
        for s in range(1, steps):
            mr = r1 + step_r * s
            mc = c1 + step_c * s
            if board[mr][mc] != EMPTY_DARK:
                return {"status": "error", "reason": "err_invalid_move"}
        new_board = [row[:] for row in board]
        new_board[r1][c1] = EMPTY_DARK
        if r2 == _promotion_row(color):
            new_board[r2][c2] = _king_of(color)
        else:
            new_board[r2][c2] = token
        return {
            "status": "ok",
            "board": new_board,
            "switch_turn": True,
            "captured": False,
            "chain_possible": False
        }
    else:
        # Adi das: 1 xana ireli (diaqonal)
        if abs(dr) != 1 or abs(dc) != 1:
            return {"status": "error", "reason": "err_invalid_move"}
        forward_dirs = _forward_directions(color)
        if (dr, dc) not in forward_dirs:
            return {"status": "error", "reason": "err_man_no_backward"}

        new_board = [row[:] for row in board]
        new_board[r1][c1] = EMPTY_DARK
        if r2 == _promotion_row(color):
            new_board[r2][c2] = _king_of(color)
        else:
            new_board[r2][c2] = token
        return {
            "status": "ok",
            "board": new_board,
            "switch_turn": True,
            "captured": False,
            "chain_possible": False
        }


# ---------------------------------------------------------------------------
# Qalib yoxlamasi
# ---------------------------------------------------------------------------

def check_win_condition(board):
    """Qaytarir: 'white', 'black' ve ya None (oyun davam edir)."""
    white_count = sum(1 for row in board for cell in row if cell in WHITE_PIECES)
    black_count = sum(1 for row in board for cell in row if cell in BLACK_PIECES)

    if white_count == 0:
        return "black"
    if black_count == 0:
        return "white"

    white_can_move = bool(
        get_all_mandatory_jumps(board, "white") or get_all_possible_moves(board, "white")
    )
    black_can_move = bool(
        get_all_mandatory_jumps(board, "black") or get_all_possible_moves(board, "black")
    )

    if not white_can_move:
        return "black"
    if not black_can_move:
        return "white"

    return None
