# This program will cover chapter 4 on loops in python
numbers = [100, 99, 98, 97, 96, 2, 4, 6, 8]
numbers.sort()

# for loop prints the list 1 line entry at a time
print("\n")
for real in numbers:
    # prints all numbers in the list after being sorted
    # loops are where indentation is key for python the same as {}; are for loops in C and C++
    print(real)
print("\n")

# to generate a numeric list without having to type in specific values use list(range(start_value, end_value, counting_value))
integers = list(range(0, 21, 2))
print(integers)

# if I wanted to generate a list of squares ** raises the value to a power of 2 
# in this code, I raise value which intial value will be one and squares it. However, with **2 I am stating that I want to square each
# term. This follows a N^2 sequence.
squares = [value**2 for value in range(0, 11)]
print(squares)
add = sum(squares)
print(add)