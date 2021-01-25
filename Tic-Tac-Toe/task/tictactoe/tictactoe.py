# write your code here
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
allFilled = False
PlayerTurn = 2


def drawGame():
    print("---------")
    for i in range(3):
        print('|', end="")
        for j in range(3):
            c = 'O' if matrix[i][j] == 1 else ('X' if matrix[i][j] == 2 else ' ')
            print(' ' + c, end="")
        print(' |')
    print("---------")


def CheckWinner(x):
    return (matrix[0][0] == x and matrix[0][1] == x and matrix[0][2] == x) or \
           (matrix[1][0] == x and matrix[1][1] == x and matrix[1][2] == x) or \
           (matrix[2][0] == x and matrix[2][1] == x and matrix[2][2] == x) or \
           (matrix[0][0] == x and matrix[1][0] == x and matrix[2][0] == x) or \
           (matrix[0][1] == x and matrix[1][1] == x and matrix[2][1] == x) or \
           (matrix[0][2] == x and matrix[1][2] == x and matrix[2][2] == x) or \
           (matrix[0][0] == x and matrix[1][1] == x and matrix[2][2] == x) or \
           (matrix[2][0] == x and matrix[1][1] == x and matrix[0][2] == x)


def CheckState():
    global matrix
    player1 = False
    player2 = False
    if CheckWinner(2):
        player2 = True
    if CheckWinner(1):
        player1 = True
    if player2 and player1:
        return "Impossible"
    elif player2:
        return "X wins"
    elif player1:
        return "O wins"
    elif all(all(i > 0 for i in x) for x in matrix):
        return "Draw"
    else:
        return "Game not finished"


def TakeInput():
    global matrix
    global PlayerTurn
    state = CheckState()
    while state == "Game not finished":
        drawGame()
        try:
            cords = input("Enter the coordinates: ")
            lis = [int(i) for i in cords.split(' ')]
            if any(x > 3 or x < 1 for x in lis):
                print("Coordinates should be from 1 to 3!")
                continue

            if not matrix[lis[0] - 1][lis[1] - 1] == 0:
                print("This cell is occupied! Choose another one!")
                continue

            matrix[lis[0] - 1][lis[1] - 1] = PlayerTurn
            PlayerTurn = 2 if PlayerTurn == 1 else 1
            state = CheckState()
        except ValueError:
            print("You should enter numbers!")
            continue
    drawGame()
    print(state)


TakeInput()
