board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "bl": " ", "bm": " ", "br": " "}


def printBoard(b):
    out = f"""{b['tl']}|{b['tm']}|{b['tr']}\n-+-+-\n{b['ml']}|{b['mm']}|{b['mr']}\n-+-+-\n{b['bl']}|{b['bm']}|{b['br']}"""

    print(out)

turn = "X"

for i in range(9):
    printBoard(board)
    print(f"{turn}'s turn.")
    position = input()
    board[position] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    
printBoard(board)
