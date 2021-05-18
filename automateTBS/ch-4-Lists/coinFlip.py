# this program will find try to find out how often a streak of six heads or six tails will come up
# from a coin flip
import random
numOfStreaks = 0
tries = 0
experimentNumber = 0
for experimentNumber in range(10000):
    coin = [] # empty list
    # code that creates a list of 100 heads or tails values
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin.append('H')
        else:
            coin.append('T')

    #code that checks if there is a steak of 6 heads or tails.
    for i in range(len(coin)):
        count = 0
        for x in range(6):
            try:
                if coin[i] == coin[i + x]:
                    count += 1
                else:
                    break
            except IndexError:
                break
        if count == 6:
            numOfStreaks += 1
    tries += 1
print('Chance of streak: %s%%' % (numOfStreaks / 100))