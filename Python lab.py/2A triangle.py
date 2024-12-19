'''Develop and test a program that determines the type of a triangle. Input sides. Output 
types is one of “not a valid triangle”, “equilateral”, “isosceles” or “scalene”.'''

s1=int (input('enter side1: '))
s2=int (input ('enter side2: '))
s3=int (input ('enter side3: '))
if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
  print ("it is a valid triangle")
  if(s1==s2==s3):
    print ('it is equilateral triangle')
  elif(s1==s2 or s1==s3 or s2==s3):
    print ('it is isosceles triangle')
  else:
    print ('it is a scalene triangle')
else:
  print ('it is not a triangle')

'''OUTPUT
enter side1: 2 enter side1:3
enter side2: 2 enter side2:6
enter side3: 2 enter side3:8
it is a valid triangle 
it is a scalene triangle
'''