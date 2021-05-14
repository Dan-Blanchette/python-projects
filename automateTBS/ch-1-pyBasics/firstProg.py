# this program says hello and asks for a name

print('Hello World!')
print('What is your name?') # ask for user's name
myName = input() # get users name
print('It is good to meet you ' + myName)
print('The length of my name is:')
print(len(myName)) # prints the number of characters for the string that was entered
print('What is your age?')
myAge = input() # get an integer number from the user
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # print user's age plus 1 year