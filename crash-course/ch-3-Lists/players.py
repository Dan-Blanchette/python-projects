# This program is an example of how list slicing is used in python
players = ['charles', 'martina', 'micheal','florence','eli']
# in this array/list the print command below returns elements 0,1, and 2 from the list
# in this case, charles martina and micheal are printed to the screen 
print(players[0:3])
# the next command will return martina micheal and florence or elements 1-4
print(players[1:4])
# by omitting the index, the print statement will print all elements including the 4th element where as having 
# two indexes means indicates the starting point of the slice
print(players[:4]) # prints 4 elements
print(players[0:5])# also prints 4 elements