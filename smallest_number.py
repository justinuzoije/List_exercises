numberList = []

howMany = int(raw_input("How many numbers?: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number: "))
    numberList.append(number)

#print numberList

min_number = min(numberList)

print min_number
