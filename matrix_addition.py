#The number of rows in the matrix is 2
matrixRowSize = 2

#The number of columns in the matrix is 2
matrixColumnSize = 2

#[1,3]
#[2,4]
firstMatrix = [[1, 3],[2, 4]]

#[5,2]
#[1,0]
secondMatrix = [[5, 2],[1, 0]]

#[0,0]
#[0,0]
newMatrix = [[0, 0],[0, 0]]

#Nested for loops are perfect for going through two-dimensional lists
#The first for loop iterates the number of times as there are rows
#Range includes 0, so we need one less than the matrix row size
for i in range(len(firstMatrix)):
#The second for loop is for accessing the data in the matrices themselves
#The range includes 0 so we need one less than the matrix column size
   for j in range(len(matrixColumnSize[0])):
#The new matrix is made of adding each individual element of the original
#matrices. Because it goes from i = 0, 1 and j = 0,1 it is accessing each
#matrix as it goes through the loop

       newMatrix[i][j] = firstMatrix[i][j] + secondMatrix[i][j]

#[[First,0],[0,0]]  0,0
#[[0,Second],[0,0]]      0,1
#[[0,0],[Third,0]]      1,0
#[[0,0],[0,Fourth]]      1,1

#To print the new matrix, print
#for r in result:
#   print(r)

print newMatrix




# # Program to add two matrices using nested loop
#
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)
