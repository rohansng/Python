'''Write a function that returns the number of digits in a string.'''

def is_digit(x):
    digit = 0
    char = 0
    for i in x:
        if i.isdigit():  # Check if the character is a digit
            digit += 1
        else:
            char += 1  # Increment character count for non-digit characters
    print('Count of characters is:', char)
    print('Count of digits is:', digit)

x = input("Enter the string:\n")
is_digit(x)

'''OUTPUT
Enter the sting
1245abcd
count of char is: 4
count of digit is : 4

Enter the sting
111
count of char is: 0
count of digit is : 3

Enter the string:
abcd
Count of characters is: 4
Count of digits is: 0
'''