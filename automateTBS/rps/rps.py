# This program runs a basic rock, paper, scissors game.

import random, sys
print('ROCK, PAPER, SCISSORS')
# these numbers keep track of wins losses and ties
wins = 0
losses = 0
ties = 0

# main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    # the players input loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # if q is entered quit the program
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break # break out of the player loop
    print('Type one of r,p,s, or q')

    # Display what player enters
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus..')

    # Display what the computer chooses
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie
    if playerMove == computerMove:
        print("it's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        wins = wins + 1
        print('You Win!')
    elif playerMove == 'p' and computerMove == 'r':
        wins = wins + 1
        print('You Win!')
    elif playerMove == 's' and computerMove == 'p':
        wins = wins + 1
        print('You Win!')
    elif playerMove == 'r' and computerMove == 'p':
        losses = losses + 1
        print('You Lose!')
    elif playerMove == 'p' and computerMove == 's':
        losses = losses + 1
        print('You Lose!')
    elif playerMove == 's' and computerMove == 'r':
        losses = losses + 1
        print('You Lose!')
