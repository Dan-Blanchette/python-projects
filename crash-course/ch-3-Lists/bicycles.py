bicycles = ['trek', 'cannodale', 'redline', 'specialized'] # to create a list in python the [] are required after variable declaration
print(bicycles) # prints the list of bikes
print(bicycles[0]) # print a specific entry from the list. In this case, bicycles[0] = trek
print(bicycles[0].title()) # formatting modifiers can also be appended to list print outs.
print(bicycles[1]) # just like an array in C++, the list position being accessed is ( n - 1 ) of the list position you want to print out
print(bicycles[3])
print(bicycles[-1]) # the negative values will print out starting with the last item of the list
message = f"\n\nMy first bicycle was a {bicycles[0].title()}" # list values can be formatted and printed
print(message)