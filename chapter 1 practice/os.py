import os

# Specify the directory you want to list (use '.' for the current directory)
directory = '/python'  # Change this to the path you want to list

# Get the list of files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)
