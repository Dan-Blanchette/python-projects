# this program will find try to find out how often a streak of six heads or six tails will come up
# from a coin flip
import random
numberOfStreaks = 0
heads = 0
tails = 0
for experimentNumber in range(1000):
    # code that creates a list of 100 'heads' or 'tails' values.
    if random.randint(0,1) == 0:
        tails += 1
        print('Tails')
        # if tails is a factor of 6, increment numberOfStreaks
        if tails % 6 == 0:
            numberOfStreaks += 1
    else:
        heads += 1
        print('Heads')
        # if heads is a factor of 6, increment numberOfStreaks
        if heads % 6 == 0:
            numberOfStreaks +=1
 
    #code that checks if there is a steak of 6 heads or tails.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))