# a brief look at lists and concatination
nums = ['1','2','3']
alpha = ['A','B','C']
newList = nums + alpha
print(newList)
for i in range(len(newList)):
    print('Index ' + str(i) + ' in newList is: ' + newList[i]) 