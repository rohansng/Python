'''Develop a program to read the contents of a text file, sort contents read and write the sorted 
contents into a separate text file.'''

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

