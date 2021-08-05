theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print("\n\nChoose a space to place your tic tac toe piece")
    print("Format = top-L, top-M, top-R, mid-L, mid-m, mid-R, low-L, low-M, low-R")
    print('Turn for ' + turn + '. Move on which space?:') 
    move = input()
    if move == "low-L" or "low-M" or "low-R" or "mid-L" or "mid-M" or "mid-R" or "top-L" or "top-M" or "top-R":
        print(move)
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        exit(1)
print('\n')
printBoard(theBoard)