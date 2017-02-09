firstList = []
secondList = []
vectorList = []

howMany = int(raw_input("How big is the list?: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number for the first list: "))
    firstList.append(number)

print ""

for i in range(howMany):
    number = int(raw_input("Please enter a number for the second list: "))
    secondList.append(number)

for i in range(howMany):
    vectorList.append(firstList[i]*secondList[i])

print vectorList
