'''Write a function that returns the number of vowels in a string.'''

def count_vowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    x = x.casefold()  # Convert the string to lowercase
    for i in x:
        if i in vowels:  # Check if the character is a vowel
            count += 1
    print("The total count of vowels is:", count) 

# Take input from the user
str1 = input('Enter the input string:\n')
count_vowels(str1)

'''OUTPUT

Enter the input string:
PythonLab

The total count of vowels is: 2
'''

def count_vowels(x):
    count = 0
    for i in x.lower():  # Use lower() method with parentheses
        if i in "aeiou":  # Corrected the condition for checking vowels
            count += 1
    return count

str1 = input('Enter the input string:\n')
print("The total count of vowels is:", count_vowels(str1))