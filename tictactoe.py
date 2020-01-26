Board = dict

def initGame():
    "Initialize a Tic Tac Toe board."
    board = {x: None for x in range(1, 10)}
    return board

def isDone(board):
    "Check if a Tic Tac Toe board is completed."
    return all([x is not None for x in board.values()])

def testIsDone():
    assert not isDone(initGame())
    assert isDone({x: 'X' for x in range(1, 10)})
    print('Success!')

testIsDone()

def printBoard(board):
    "Display a pretty print of a Tic Tac Toe board."
    rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in rows:
        print(' {} | {} | {}'.format(
            *[board[col] if board[col] is not None else ' '
              for col in row]))
        if row != rows[-1]:
            print('-'*10)
    print('\n\n')

printBoard(initGame())
board = initGame()
board[5] = 'X'
printBoard(board)

def printInputBoard(board):
    "Print a board with numbers to help with input."
    inpBoard = {x: x if board[x] is None else board[x] for x in range(1, 10)}
    printBoard(inpBoard)

printInputBoard(board)

def playGame():
    "Play a game of Tic Tac Toe"
    board = initGame()
    for play in range(1, 10):
        printInputBoard(board)
        player = 'O' if play % 2 == 0 else 'X'
        move = int(input("Player {}, select an open position on the board: ".format(player)))
        board[move] = player
        winner = checkWinner(board)
        if winner is not None:
            print('Player {} wins!'.format(winner))
            break
    if winner is None:
        printBoard(board)
        print("It's a tie!")
    playAgain = input("Would you like to play again? ('Y' or 'N'): ")
    if playAgain == 'Y': playGame()

winPositions = [
    (1, 2, 3),
    (1, 4, 7),
    (1, 5, 9),
    (3, 5, 7),
    (3, 6, 9),
    (2, 5, 8),
    (4, 5, 6),
    (7, 8, 9)]

def checkWinner(board):
    "Check if a player has won the game."
    for winPosition in winPositions:
        if all([board[x] == 'O' for x in winPosition]): return 'O'
        if all([board[x] == 'X' for x in winPosition]): return 'X'
    return None

#playGame()

def openPos(board):
    """Determine what positions are open on the tic tac toe board and return
    as a list."""
    return [x for x in board.keys() if board[x] is None]

def testOpenPos():
    board = initGame()
    board[5] = 'X'
    assert openPos(board) == [1, 2, 3, 4, 6, 7, 8, 9]
    board[9] = 'O'
    assert openPos(board) == [1, 2, 3, 4, 6, 7, 8]
    print('Works!')

def oppPos(board):
    "Opponent is always `X`, return their positions on a tic tac toe board."
    return [x for x in board.keys() if board[x] == 'X']

def checkForBlockOrWin(oppPos, openPos):
    """Check an opponents position and see if we need to block them from winning.
    Return a positoin to block else return None."""
    if len(oppPos) == 1: return None
    op = set(oppPos)
    for winPos in winPositions:
        wp = set(winPos)
        inter = wp & op
        remainder = (wp - inter).pop()
        if len(inter) == 2 and remainder in openPos:
            return remainder
    return None

def testc4block():
    board = initGame()
    board[3] = 'X'
    board[7] = 'X'
    assert checkForBlockOrWin(oppPos(board), openPos(board)) == 5
    board[5] = 'O'
    assert checkForBlockOrWin(oppPos(board), openPos(board)) is None
    print('Works!')

def ourPos(board):
    "We are always `O`, retrun our positions on a tic tac toe board."
    return [x for x in board.keys() if board[x] == 'O']

import random

def makeMove(board):
    "Determine the next move to make on a tic tac toe board and return the new board."
    opn = openPos(board)
    if opn == []: return board
    opp = oppPos(board)
    our = ourPos(board)
    win = checkForBlockOrWin(our, opn)
    if win is not None:
        board[win] = 'O'
        return board
    blk = checkForBlockOrWin(opp, opn)
    if blk is not None:
        board[blk] = 'O'
        return board
    if 5 in opn:
        board[5] = 'O'
        return board
    cond = (len(set(opp) & {1, 9}) == 2 or
            len(set(opp) & {3, 7}) == 2)
    if len(set(opn) & {1, 3, 7, 9}) > 0 and not (len(opn) == 6 and cond):
        while True:
            pos = random.choice([1, 3, 7, 9])
            if pos in opn:
                board[pos] = 'O'
                return board
    elif (len(opn) == 6 and cond):
        while True:
            pos = random.choice([2, 4, 6, 8])
            if pos in opn:
                board[pos] = 'O'
                return board
    while True:
        pos = random.choice(range(1, 10))
        if pos in opn:
            board[pos] = 'O'
            return board

testOpenPos()
testc4block()

def playGameWithAI():
    "Play a game of Tic Tac Toe with an AI player."
    board = initGame()
    for play in range(1, 6):
        if openPos(board) == []: break
        printInputBoard(board)
        move = int(input("Player X, select an open position on the board: "))
        board[move] = 'X'
        winner = checkWinner(board)
        if winner is not None:
            print('Player {} wins!'.format(winner))
            break
        board = makeMove(board)
        winner = checkWinner(board)
        if winner is not None:
            print('Player {} wins!'.format(winner))
            break
    if winner is None:
        printBoard(board)
        print("It's a tie!")
    playAgain = input("Would you like to play again? ('Y' or 'N'): ")
    if playAgain == 'Y': playGameWithAI()

playGameWithAI()
            
