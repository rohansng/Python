'''Develop a program that computes the power of a number N and prints the result. Input N.
Hint: program uses a loop construct.'''


#Calculate power of a number using a while loop
base = int(input("Enter the base value : \n"))
exponent = int(input('Enter the exponent value \n'))
result = 1
while exponent != 0 :
    #result *= base
    result = result * base
    exponent =exponent-1
print("Answer = " + str(result))
#Calculate power of a number using a for loop
base = int(input("Enter the base value : \n"))
exponent = int(input('Enter the exponrnt value : \n'))
result = 1
for exponent in range(exponent, 0, -1):
    result *= base
print("Answer = " + str(result))


'''OUTPUT
Enter the base value :
2
Enter the exponrnt value
3
Answer = 8'''