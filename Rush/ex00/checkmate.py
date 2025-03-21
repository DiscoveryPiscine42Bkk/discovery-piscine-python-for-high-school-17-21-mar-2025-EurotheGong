def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "K":
                return row, col
    return None

def is_under_attack(board, row, col):
    directions = {
        "Rook": [(0,1), (0,-1), (1,0), (-1,0)],
        "Bishop": [(1,1), (1,-1), (-1,1), (-1,-1)],
        "Queen": [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    }

    for piece, moves in directions.items():
        for dr, dc in moves:
            r, c = row, col
            while 0 <= r + dr < len(board) and 0 <= c + dc < len(board[0]):
                r += dr
                c += dc
                if board[r][c] == ".":
                    continue
                elif board[r][c] in ["R", "B", "Q"]:
                    if (piece == "Rook" and board[r][c] == "R") or \
                       (piece == "Bishop" and board[r][c] == "B") or \
                       (piece == "Queen" and board[r][c] == "Q"):
                        return True
                break
    return False

def is_checkmate(board):
    king_pos = find_king(board)
    if not king_pos:
        return False

    row, col = king_pos

    if not is_under_attack(board, row, col):
        return False  

    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            if board[new_row][new_col] == "." and not is_under_attack(board, new_row, new_col):
                return False

    return True
