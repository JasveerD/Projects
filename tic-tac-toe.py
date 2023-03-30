board = [['X','O','X'], ['X','O','-'], ['O','-','O']]
turn = 0

def showBoard():
    print(board[0][0] + '  |  ' + board[0][1] + '  |  ' + board[0][2])
    print('---+-----+---')
    print(board[1][0] + '  |  ' + board[1][1] + '  |  ' + board[1][2])
    print('---+-----+---')
    print(board[2][0] + '  |  ' + board[2][1] + '  |  ' + board[2][2])

def turnInput():
    row = input("Enter row: ")
    col = input("Enter column: ")
    return [int(row)-1, int(col)-1]

def xTurn():
    print('X turn')
    coordinate = turnInput()
    if board[coordinate[0]][coordinate[1]] == '-':
        board[coordinate[0]][coordinate[1]] = 'X'
        showBoard()
        winCheck(board)
        oTurn()

    else:
        print('Invalid Input')
        xTurn()

def oTurn():
    print('O turn')
    coordinate = turnInput()
    if board[coordinate[0]][coordinate[1]] == '-':
        board[coordinate[0]][coordinate[1]] = 'O'
        showBoard()
        winCheck(board)
        xTurn()
    else:
        print('Invalid Input')
        oTurn()

def rowWinCheck(gameBoard):
    for i in range(len(gameBoard)):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] == 'X':
            print('X wins!')
            exit()
        elif gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] == 'O':
            print('O wins!')
            exit()
        else:
            pass

def colWinCheck(gameBoard):
    for i in range(len(gameBoard)):
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] == 'X':
            print('X wins!')
            exit()
        elif gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] == 'O':
            print('O wins!')
            exit()
        else:
            pass

def diagWinCheck(gameBoard):
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'X':
        print('X wins!')
        exit()

    elif gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'O':
        print('O wins!')
        exit()

    elif gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == 'X':
        print('X wins!')
        exit()

    elif gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == 'O':
        print('O wins!')
        exit()

    else:
        pass

def drawCheck(gameBoard):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'X' or board[i][j] == 'O':
                count = count + 1
    if count == 9:
        print('Draw!')
        exit()

def winCheck(gameBoard):
    drawCheck(gameBoard)
    rowWinCheck(gameBoard)
    colWinCheck(gameBoard)
    diagWinCheck(gameBoard)


while True:
    showBoard()
    xTurn()
