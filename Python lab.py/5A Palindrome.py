'''Develop a function that returns true if input string is a palindrome; otherwise it returns 
false.'''

def check_palindrome(string):
    revstr = ""  # Initialize an empty string to store the reversed string
    for i in string:
        revstr = i + revstr  # Append each character in reverse order
    print("Reversed string:", revstr)
    if string == revstr:  # Compare the original string with the reversed string
        return True
    else:
        return False

input_string = input("Enter a string: ")
if check_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''def isPalindrome(st):
    return st == st[::-1]  # Compare the string with its reverse

s = input("Enter a string: ")  # Take input from the user

ans = isPalindrome(s)  # Call the function with the input string

if ans:
    print("True")  # Print True if the string is a palindrome
else:
    print("False")  # Print False if the string is not a palindrome'''


'''OUTPUT

Enter a string: MOM 
Reversed string: MOM
True

Enter a string: PythonLab
Reversed string: baLnohtyP
False
'''





