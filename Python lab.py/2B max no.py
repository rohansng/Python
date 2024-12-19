'''Develop a program to print the maximum of five numbers. Input five numbers and print 
the maximum.'''
 
print ("Enter the five numbers")
num1 = int (input ('Enter the number1 : '))
num2 = int (input ('Enter the number2 : '))
num3 = int (input ('Enter the number3 : '))
num4 = int (input ('Enter the number4 : '))
num5 = int (input ('Enter the number5 : '))
if num1>=num2 and num1>=num3 and num1>= num4 and num1>=num5: 
 print ('number 1 is largest',num1)
elif num2>=num1 and num2>=3 and num2>= num4 and num2>=num5 :
 print ('number 2 is largest',num2)
elif num3>=num1 and num3>=num2 and num3>= num4 and num3>=num5 :
 print ('number 3 is largest',num3)
elif num4>=num1 and num4>=num2 and num4>= num3 and num4>=num5 :
 print ('number 4 is largest : ',num4)
else:
 print ('number 5 is largest',num5)
 
'''OUTPUT
Enter the five numbers
Enter the number1 : 2
Enter the number2 : 3
Enter the number3 : 1
Enter the number4 : 5
Enter the number5 : 4
number 4 is largest : 5'''