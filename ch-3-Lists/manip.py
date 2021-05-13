# this list lesson will cover list manipulation
motorbikes = ['yamaha', 'honda', 'suzuki']
message = f"This is the original list {motorbikes}."
print(message)

# append('') adds a new entry to the list
motorbikes.append('ducati') 
message1 = f"I had an impulse buy so I bought a ducati and added it to my list {motorbikes}."

print(message1)
# swaps ducati to be the first of the list
motorbikes.insert(0, 'ducati') 

# remove the second entry of ducati from the end
del motorbikes[-1]

# popping removes the value at the end of the list
message2 = f"The ducati is my new favorite out of all my bikes. I am going to put make it the first bike on my list{motorbikes}."
print(message2)

# removes the list entry from the end of the list and stores the removed entry in the variable popped_motorbikes
popped_motorbikes = motorbikes.pop() 
soldBike = f"I just sold a motorcyle it was my {popped_motorbikes}."  
print(soldBike)

# reprint the new list after all the modifications
newlist = f"Now all I have are my: {motorbikes[0].title()}, {motorbikes[1].title()}, and {motorbikes[2].title()}."
print(newlist)

# using .remove('') allows for a specified value stated between the '' to be removed from the list
soldBike = f"Oh no, I couldn't afford the {motorbikes[0].title()} and it got reposessed."

# assigns a varible to hold the value ducati
tooExpensive = 'ducati'
# removes ducati from the list based on the value of tooExpensive which is currently ducati
motorbikes.remove(tooExpensive)
print(soldBike)

#print the updated list values
newlist = f"Now all I have is my {motorbikes[0].title()} and {motorbikes[1].title()}."
print(newlist)