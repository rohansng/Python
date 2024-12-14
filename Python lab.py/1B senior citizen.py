'''Develop a program to read the name and year of the birth of a person. Display whether the 
person is a senior citizen or not.'''

y=input ("Enter the name of the person: \n")
x=int (input ("Enter the year of birth: \n"))
current_year = int(input("Enter current year : \n"))
age=current_year-x
if(age>=60):
 print (y," is a Senior citizen")
else:
 print (y," is Not a senior citizen")

'''OUTPUT

Enter the name of the person: abc
Enter the year of birth: 1960
Enter current year: 2023
abc is a Senior citizen'''