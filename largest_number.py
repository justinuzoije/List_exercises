numberList = []

howMany = int(raw_input("How many numbers?: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number: "))
    numberList.append(number)

#print numberList

max_number = max(numberList)

print max_number
