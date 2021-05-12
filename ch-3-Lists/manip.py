# this list lesson will cover list manipulation
motorbikes = ['yamaha', 'honda', 'suzuki']
message = f"This is the original list {motorbikes}"
print(message)
motorbikes.append('ducati') # append('') adds a new entry to the list
message1 = f"I had an impulse buy so I bought a ducati and added it to my list {motorbikes}"
print(message1)
motorbikes.insert(0, 'ducati') # swaps ducati to be the first of the list
del motorbikes[-1]
message2 = f"The ducati is my new favorite out of all my bikes. I am going to put make it the first bike on my list{motorbikes}"
print(message2)
popped_motorbikes = motorbikes.pop()
soldBike = f"I just sold a motorcyle it was my {popped_motorbikes}"
print(soldBike)
newlist = f"Now all I have are my: {motorbikes[0].title()}, {motorbikes[1].title()}, and {motorbikes[2].title()}"
print(newlist)
