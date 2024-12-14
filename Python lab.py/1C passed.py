'''Develop a program to read USN, Name and marks in three subjects. Print USN, Name of 
student, total marks and percentage. Print number of subjects in 1C in which student has 
passed.'''

name=input ('Enter the name of the student:')
usn=input ('Enter the usn of the student:')
print (" ")
print ('Enter marks in 3 subjects')
phy_marks=int (input("Enter marks of the first subject: "))
chem_marks=int (input("Enter marks of the second subject: "))
maths_marks=int (input("Enter marks of the third subject: "))
print ("")
total=phy_marks + chem_marks + maths_marks
percentage=(total/300) *100
print ('Name of the student is',name)
print('USN',usn)
print ('The total is',total,'and the percentage is',percentage)
print (" ")
if(phy_marks>=40 and chem_marks>=40 and maths_marks>=40):
 print ('Student has passed in all three subjects')
elif((phy_marks>=40 and chem_marks>=40) or (chem_marks>=40 and maths_marks>=40) or 
(phy_marks>=40 and maths_marks>=40)):
 print ('Student has passed in two subjects')
elif(phy_marks>=40 or chem_marks>=40 or maths_marks>=40):
 print ('Student has passed in only one subjects')
#elif ((phy_marks<40 or chem_marks<40 or maths_marks<40)):
else:
 print ('Student has not passed in any subject')


'''Output

Enter the name of the student: abc
Enter the usn of the student :123 
Enter marks in 3 subjects 
Enter marks of the first subject: 50 
Enter marks of the second subject: 60 
Enter marks of the third subject: 100

Name of the student is abc
USN 123 
The total is 210 and the percentage is 70.0 
Student has passed in all three subjects'''