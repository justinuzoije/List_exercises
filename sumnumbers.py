numberList = []

howMany = int(raw_input("How many numbers?: "))

for i in range(howMany):
    number = int(raw_input("Please enter a number: "))
    numberList.append(number)

#print numberList

sum_numbers = sum(numberList)

print sum_numbers
