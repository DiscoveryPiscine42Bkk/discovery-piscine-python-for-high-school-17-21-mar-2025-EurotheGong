from checkmate import is_checkmate

def parse_board(board_str):
    return [list(row) for row in board_str.strip().split("\n")]

def is_valid_board(board_list):
    if not board_list:
        return False
    width = len(board_list[0])
    return all(len(row) == width for row in board_list)

def main():
    board = """\
RB..
.RKR
....
.R..\
"""

    board_list = parse_board(board)  

    if not is_valid_board(board_list):
        print("❌ Error: Invalid board! The board must be a rectangle.")
        return

    if is_checkmate(board_list):
        print("Success")
    else:
        print("Fail")

if __name__ == "__main__":
    main()
