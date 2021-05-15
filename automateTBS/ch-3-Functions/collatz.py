# this programm will generate the collatz sequence
def collatz(number):
    # if the number entered is a factor of 2 with no remainder it's even.
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # else if the number entered has a remainder of 1 it is odd.
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

userNum = input("Please enter a number: ")
print(userNum)

while userNum != 1:
    userNum = collatz(int(userNum))