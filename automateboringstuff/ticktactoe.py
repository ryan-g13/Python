# Basic tick tac toe game does not detect winner will kick if second guess overwrites a previous guess.

gameBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' ' }

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])
turn = 'X'
for i in range(9):
    printBoard(gameBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    gameBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printBoard(gameBoard)
