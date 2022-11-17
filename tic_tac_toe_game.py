from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

board[1][1] = 'X'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def display_board(board):
    print(bcolors.WARNING + "+-------+-------+-------+")
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "+-------+-------+-------+")
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "+-------+-------+-------+")
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))
    print(bcolors.WARNING + "|       |       |       |")
    print(bcolors.WARNING + "+-------+-------+-------+" + bcolors.ENDC)

def bys():
    print(bcolors.FAIL + "\nwe are waiting for you again")
    print(bcolors.FAIL + "         ____")
    print(bcolors.FAIL + "       _(____)_")
    print(bcolors.FAIL + "___ooO_(_o__o_)_Ooo___")

def enter_move(board):
    while True:
        try:
            inpt = int(input("where would you like to move? (q = -1) ->  ")) - 1
        except:
            print("No Input")
            continue
        if (inpt == -2):
            bys()
            exit()
        if (inpt < 0 or inpt > 8):
            print("Your entry should be between 1 and 9")
            continue
        elif (board[inpt // 3 ][inpt % 3] in ['O','X']):
            print("Field already occupied - repeat your input")
            continue
        else:
            break
    board[inpt // 3 ][inpt % 3] = 'O'

def make_list_of_free_fields(board):
    result = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] in ['O','X']:
                result += 1
    return (result)


def victory_for(board, sign):
    if (not sign):
        return None
    corner = True
    cornerLeft = True
    for idx in range(3):
        if (board[0][idx] == sign and board[1][idx] == sign \
            and board[2][idx] == sign):
            return (sign)
        if (board[idx][0] == sign and board[idx][1] == sign \
            and board[idx][2] == sign):
            return (sign)
        if (board[idx][idx] != sign):
            corner = False
        if (board[2 - idx][2 - idx] != sign):
            cornerLeft = False
    if corner or cornerLeft:
        return (sign)
    return (None)

def draw_move(board):
    for i in range(10):
        pcMove = randrange(8) - 1
        if (pcMove <1 or pcMove > 9):
            continue
        elif (board[pcMove // 3 ][pcMove % 3] in ['O','X']):
            continue
        else:
            break
    board[pcMove // 3 ][pcMove % 3] = 'X'

freeField = make_list_of_free_fields(board)
winner = None
while (freeField):
    display_board(board)
    enter_move(board)
    winner = victory_for(board, 'O')
    if (winner):
        break
    draw_move(board)
    winner = victory_for(board, 'X')
    if (winner):
        break
display_board(board)
if winner == "O":
	print(bcolors.OKBLUE + "You won!")
elif winner == 'X':
	print(bcolors.WARNING + "I won")
else:
	print("Tie!")