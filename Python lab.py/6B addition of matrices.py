'''Develop a program to add two matrices represented using Python lists.'''
L1 = [[1, 2, 5], [4, 3, 1], [2, 6, 8]]
L2 = [[3, 6, -1], [2, 9, 5], [1, 6, 0]]
Result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Perform matrix addition
for i in range(len(L1)):
    for j in range(len(L1[0])):
        Result[i][j] = L1[i][j] + L2[i][j]

# Print the result
print('Addition of two matrices:')
for i in range(3):
    for j in range(3):
        print(Result[i][j], end=' ')
    print()

'''
OUTPUT
Addition of two matrices
4 8 4
6 12 6
3 12 8
'''