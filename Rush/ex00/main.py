from checkmate import is_checkmate

def main():
    board = """\
    R...
    .K..
    ..Q.
    ....\
    """

    if is_checkmate(board):
        print("Success")
    else:
        print("Fail")

if __name__ == "__main__":
    main()
