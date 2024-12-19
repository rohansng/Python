'''Develop a program that inputs names of five students and displays if your name is present 
in the five names.'''

myName=input ('enter your name: \n')
naMe1=input ('enter the name 1 : \n')
naMe2=input ('enter the name 2 : \n')
naMe3=input ('enter the name 3 : \n')
naMe4=input ('enter the name 4 : \n')
naMe5=input ('enter the name 5 : \n')
if (myName == naMe1) or (myName == naMe2) or (myName == naMe3) or (myName == 
naMe4) or (myName == naMe5 ):
 print ("hi u r name is : ",myName)
else:
 print (" your name is not present in five names")
 
 '''OUTPUT

enter your name: abc 
enter the name 1: xyz 
enter the name 2: lmn 
enter the name 3: pqr 
enter the name 4: abc 
enter the name 5: def 
hi u r name is: abc 
'''