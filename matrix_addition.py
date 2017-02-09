#firstMatrix = [[0,0],[0,0]]
#secondMatrix = [[0,0],[0,0]]
addedMatrix = [[0,0],[0,0]]

#listDimension = int(raw_input("What is the matrix dimension?: "))

#2 rows 2 columns

firstMatrix = [[1,3],[2,4]]
secondMatrix = [[5,2],[1,0]]

for row in firstMatrix:
    for col in firstMatrix:
        addedMatrix.append(firstMatrix[row]+secondMatrix[row])

print addedMatrix
