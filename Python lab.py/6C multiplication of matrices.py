'''Develop a program to multiply two matrices using Python lists.'''
L1 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
L2 = [[1, 2, 1], [2, 2, 3], [3, 2, 1]]
Result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Iterate through rows of L1
for i in range(len(L1)):
    # Iterate through columns of L2
    for j in range(len(L2[0])):
        # Iterate through rows of L2
        for k in range(len(L2)):
            Result[i][j] += L1[i][k] * L2[k][j]

print('Multiplication of two matrices:')
for i in range(len(Result)):
    for j in range(len(Result[0])):
        print(Result[i][j], end=' ')
    print()

'''
OUTPUT
Multiplication of two matrices
14 12 10 
20 18 15 
26 24 20
'''