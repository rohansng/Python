'''Develop a program that prints the first N numbers of Fibonacci sequence. Input N.
Hint: program uses a loop construct.'''

nterms = int(input('How many terms? '))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

'''OUTPUT
how many terms? -1 
please enter a positive 

how many terms? 4
Fibonacci sequence:
0
1
1
2
'''