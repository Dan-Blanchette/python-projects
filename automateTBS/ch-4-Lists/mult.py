# tricks with lists
# random library
import random

# multiple assignment trick
dog = ['healthy', 'black', 'lab']
medical, color, species = dog
# print(medical, color, species)

# enumerate
for index, item in enumerate(dog):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# changes the order in the list
random.shuffle(dog)
# print out the new order
print(dog)

# finding the index after the list is randomized
dex = dog.index('black')
print(dex)