'''Develop a program that computes the factorial of a number N and prints the result. Input N. 
Hint: Program uses a loop construct.'''

# Using while loop to calculate factorial
n = int(input("Enter any number: "))
fact = 1
i = 1

if n < 0:
    print("Enter a Positive Integer!")
elif n == 0 or n == 1:
    print("The factorial of a number is: 1")
else:
    while i <= n:
        fact = fact * i
        i = i + 1
    print("The factorial of a number is:", fact)

'''OUTPUT

enter the number: -1
enter positive number 
'''

#2nd option
#Using for loop
n=int(input("Enter any number: "))
if(n<0):
    print("Enter a Positive Integer!")
elif(n==0 or n==1):
    print("the factorial of a number is:",1)
else:
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    print("factorial of a given number is:",fact)

'''OUTPUT

enter the number: 5
factorial of a given number is: 120
'''