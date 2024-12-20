'''Develop a program to add two sparse matrices. Hint: Use a Dictionary.'''

matrix1 = [
    [0, 0, 0, 1, 0],
    [2, 0, 0, 0, 3],
    [0, 0, 0, 4, 0]
]

matrix2 = [
    [0, 1, 0, 4, 0],
    [0, 0, 0, 3, 0],
    [1, 4, 0, 0, 2]
]

def convertToDictionary(matrix):
    dct = {}
    for i in range(len(matrix)):  # Iterate through rows
        for j in range(len(matrix[0])):  # Iterate through columns
            if matrix[i][j] != 0:  # Include non-zero elements
                dct[(i, j)] = matrix[i][j]  # Store as key-value pair
    return dct

dictionaryMatrix1 = convertToDictionary(matrix1)
dictionaryMatrix2 = convertToDictionary(matrix2)

def addSparseMatrix(first, second):
    resultantDict = {}
    #allKeys = set(first.keys()).union(second.keys())  # Combine keys from both dictionaries
    allkeys=list(first.keys())+list(second.keys())
    for keyIterator in allkeys:
        firstValue = first.get(keyIterator, 0)
        secondValue = second.get(keyIterator, 0)
        sumOfValues = firstValue + secondValue
        if sumOfValues != 0:  # Only include non-zero sums
            resultantDict[keyIterator] = sumOfValues
    return resultantDict

res = addSparseMatrix(dictionaryMatrix1, dictionaryMatrix2)
print(res)

'''
OUTPUT
{(0, 3): 5, (1, 0): 2, (1, 4): 3, (2, 3): 4, (0, 1): 1, (1, 3): 3, (2, 0): 1, (2, 1): 4, (2, 4): 2}

'''