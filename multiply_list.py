numberList = []
multipliedList = []

howMany = int(raw_input("How many numbers?: "))
theFactor = int(raw_input("Please enter a factor: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number: "))
    numberList.append(number)

for i in numberList:
    multipliedNumber = i * theFactor
    multipliedList.append(multipliedNumber)

print multipliedList
