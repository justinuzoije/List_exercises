numberList = []
posNumbers = []

howMany = int(raw_input("How many numbers?: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number: "))
    numberList.append(number)

for i in numberList:
    if i > 0:
        posNumbers.append(i)

print posNumbers
