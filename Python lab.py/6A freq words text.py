'''Develop a program to print 10 most frequently appearing words in a text file. Use 
dictionary data type'''

import os
# Dictionary to store word counts
wordCounts = {}
# Open the file 'sample.txt' in read mode
fileHandler = open("D:\Python\sample.txt.rtf")
# Function to remove punctuations from a string
def removePunctuations(string):
    PUNCTUATIONS = "!()-[]{}\\,./?@#$%^&*_~"
    for ele in string:
        if ele in PUNCTUATIONS:
            string = string.replace(ele, ' ')
    return string

# Read each line in the file
for line in fileHandler:
    # Remove punctuations and convert to lowercase
    line = removePunctuations(line).lower()
    # Split line into words and count occurrences
    for word in line.split():
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

# Close the file
#fileHandler.close()

# Create a list of (count, word) tuples
lst = []
for key, val in list (wordCounts.items()):
    lst.append((val, key))

# Sort the list in descending order of counts
lst.sort(reverse=True)

# Create the final list with (word, count) format
finalList = []
for val, key in lst:
    finalList.append((key, val))

# Print the top 10 most frequent words as a dictionary
print(dict(finalList[0:10]))


'''
OUTPUT

'''