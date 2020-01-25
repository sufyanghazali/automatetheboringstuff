import random

wins = 0
losses = 0
ties = 0
moves = ["r", "p", "s", "q"]


def versus(player_move):
    global wins, losses, ties

    comp_move = gen_comp_move()
    print_player_move(eval_move(player_move))
    print(f"{eval_move(comp_move)}")
    win_status = result(player_move, comp_move)
    print(f"{win_status}!")
    update_score(win_status)
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")


def result(player, comp):
    win_status = ""

    if player == comp:
        win_status = "Tie"
    elif player == "r":
        if comp == "s":
            win_status = "Win"
        elif comp == "p":
            win_status = "Lose"
    elif player == "p":
        if comp == "r":
            win_status = "Win"
        elif comp == "s":
            win_status = "Lose"
    elif player == "s":
        if comp == "p":
            win_status = "Win"
        elif comp == "r":
            win_status = "Lose"

    return win_status


def update_score(status):
    global wins, losses, ties
    if status == "Win":
        wins += 1
    elif status == "Lose":
        losses += 1
    elif status == "Tie":
        ties += 1


def input_user_move():
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    move = input()

    while not move or move not in moves:
        print("Enter a valid input dickhead")
        move = input()

    return move.lower()


def gen_comp_move():
    return moves[random.randint(0, 2)]


def eval_move(move):
    moveStr = ""

    if move == "r":
        moveStr = "ROCK"
    elif move == "p":
        moveStr = "PAPER"
    elif move == "s":
        moveStr = "SCISSORS"

    return moveStr


def print_player_move(moveStr):
    print(f"{moveStr} versus...")


def play():
    player = input_user_move()
    while player != "q":
        versus(player)
        player = input_user_move()


def main():
    print("ROCK, PAPER, SCISSORS")
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    play()

main()
