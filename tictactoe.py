import os

chanceOfFirst = True
size = 3
board = []

def initialise():
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(-1)
        board.append(row)

def check():
    '''
    Return -1 if no one is winning, 0 if draw, 1 is player 1 wins,
    2 if player 2 wins
    '''
    # check draw
    count = 0
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] is not -1:
                count += 1
    if count is 9:
        return 0
    
    # check colums
    for i in range(0, size):
        if board[i] == [0, 0, 0]:
            return 1
        elif board[i] == [1, 1, 1]:
            return 2

    # checks rows
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(board[j][i])
        if row == [0, 0, 0]:
            return 1
        elif row == [1, 1, 1]:
            return 2
            
    # check diagonals

    # left diagonal
    diagonal = []
    for i in range(0, size):
        diagonal.append(board[i][i])
    if diagonal == [0, 0, 0]:
        return 1
    elif diagonal == [1, 1, 1]:
        return 2

    # right diagonal
    diagonal = []
    for i in range(0, size):
        diagonal.append(board[i][size - i - 1])
    if diagonal == [0, 0, 0]:
        return 1
    elif diagonal == [1, 1, 1]:
        return 2

    # else return no result yet
    return -1

def display():
    '''
    Displays the board and fetches the position from the user.
    '''
    global chanceOfFirst
    global board

    os.system('cls')

    print("Player ", end = '')
    if chanceOfFirst:
        print("1 (O)")
    else:
        print("2 (X)")

    print(" ", end = ' ')
    for j in range(0, size):
        print(j + 1, end = ' ')
    print()
    for i in range(0, size):
        print(i + 1, end = ' ')
        for j in range(0, size):
            if board[i][j] is -1:
                print("_", end = ' ')
            elif board[i][j] is 0:
                print("O", end = ' ')
            elif board[i][j] is 1:
                print("X", end = ' ') 
        print()

    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    while (x > size and x < 0) or (y > size or y < 0):
        print("Position specified is wrong.")
        wait = input("Press enter to continue...")
        display()

    while board[y - 1][x - 1] is not -1:
        print("Cheating not allowed! :)")
        wait = input("Press enter to continue...")
        display()
       
    if chanceOfFirst:
        board[y - 1][x - 1] = 0
    else:
        board[y - 1][x - 1] = 1

    if chanceOfFirst:
        chanceOfFirst = False
    else:
        chanceOfFirst = True

    return check()
            
initialise()
while True:
    whoWon = display()
    if whoWon is 1:
        print("Player 1 wins!")
        wait = input("Press enter to exit...")
        break
    elif whoWon is 2:
        print("Player 2 wins!")
        wait = input("Press enter to exit...")
        break
    elif whoWon is 0:
        print("Its a draw!")
        wait = input("Press enter to exit...")
        break
