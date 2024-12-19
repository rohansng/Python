'''Write a function that outputs the number obtained by reversing the digits of a number'''

def reverse_number(n):
    r = 0
    while n > 0:
        d = n % 10
        r = r * 10 + d
        n = n // 10
    return r

n = int(input("Enter number: "))  # Fixed the quotes
r = reverse_number(n)
print("Reversed number is:", r)

'''
OUTPUT
enter number 123
Reversed number is : 321
'''