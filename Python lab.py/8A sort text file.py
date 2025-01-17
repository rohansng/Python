'''Develop a program to read the contents of a text file, sort contents read and write the sorted 
contents into a separate text file.'''

import os

# Open the file for reading
fhand = open('1.txt', 'r')
content = fhand.read()
fhand.close()  # Close the file after reading

# Process the content
content = content.split('\n')  # Split content into lines
content.sort()  # Sort the lines alphabetically

# Open another file for writing
fhand = open('write.txt', 'w')
for word in content:
    fhand.write(word + '\n')  # Write each sorted line to the new file
fhand.close()  # Close the file after writing




'''
# Import necessary module
import os

# Input and output file paths
input_file = '1.txt'
output_file = 'write.txt'

# Check if the input file exists
if os.path.exists(input_file):
    # Read the contents of the input file
    with open(input_file, 'r') as fhand:
        content = fhand.read().splitlines()  # Read lines and split them into a list

    # Sort the contents
    content.sort()

    # Write the sorted contents to the output file
    with open(output_file, 'w') as fhand:
        for line in content:
            fhand.write(line + '\n')

    print(f"Contents sorted and written to '{output_file}'.")
else:
    print(f"Error: File '{input_file}' does not exist.")
'''
