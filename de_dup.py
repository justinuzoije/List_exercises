theList = [1,4,4,5,4,4,11,11]

newList = []

for i in theList:
    if i not in newList:
        newList.append(i)

print newList
