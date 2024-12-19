'''Input a multi-digit number (as chars) and develop a program that prints the frequency of 
each digit with suitable messages.'''

n = input("Enter the number: ")

digit = input("Num to find the occurrence: ")

def freq():
    count = 0
    for i in n:
        if i == digit:
            count += 1
    print(count)

freq()

'''
OUTPUT
Enter the number: 111233
Num to find the occurrence: 1
3
'''

def char_frequency(str1):
    # Initialize an empty dictionary
    dict = {}
    
    # Loop through each character in the string
    for n in str1:
        # Check if the character is already in the dictionary
        if n in dict:
            dict[n] += 1  # Increment the count
        else:
            dict[n] = 1  # Initialize the count
    return dict

# Input from the user
a = input('Enter the number: ')

# Print the character frequency
print(char_frequency(a))

'''
OUTPUT
Enter the number: 111233
{'1': 3, '2': 1, '3': 2}
'''