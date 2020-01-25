test = {'1z': 'bking', '6c': 'wqueen',
        '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


def createBoard():
    row = "abcdefgh"
    col = "12345678"
    board = {}

    for i in row:
        for j in col:
            board[i+j] = " "

    return board


def isValidChessBoard(board):

    isValid = True
    pieces = list(board.values())
    spaces = list(board.keys())
    white = [piece for piece in pieces if piece[0] == "w"]
    black = [piece for piece in pieces if piece[0] == "b"]

    isValid = isValidSpaces(spaces) and isValidPieces(
        pieces) and isValidTeams(black, white)

    return isValid


def isValidSpaces(pieces):
    isValid = True
    i = 0

    while isValid and i < len(pieces):
        isValid = int(pieces[i][0]) > 0 and int(
            pieces[i][0]) < 9 and pieces[i][1] > "Z" and pieces[i][1] < "i"
        i += 1

    return isValid


def isValidPieces(pieces):
    isValid = True
    i = 0
    while isValid and i < len(pieces):
        isValid = pieces[i][0] == 'w' or pieces[i][0] == "b"
        i += 1
    return isValid


def isValidTeams(black, white):
    return validTeamCount(black, white) and validPawnCount(black, white) and validKingCount(black, white)


def validTeamCount(black, white):
    bCount = len(black)
    wCount = len(white)
    return validNumber(0, 16, bCount) and validNumber(0, 16, wCount)


def validPawnCount(black, white):
    bPawn = black.count("bpawn")
    wPawn = white.count("wpawn")
    return validNumber(0, 8, bPawn) and validNumber(0, 8, wPawn)


def validKingCount(black, white):
    bKing = black.count("bking")
    wKing = white.count("wking")
    return bKing == 1 and wKing == 1


def validNumber(min, max, list):
    return list >= min and list <= max


print(isValidChessBoard(test))
