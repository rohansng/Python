'''Develop Python programs to convert Centigrade temperature into Fahrenheit and to
convert Fahrenheit temperature into Centigrade.'''

# Centigrade temperature into Fahrenheit
c=float (input ('Enter temperature in Centigrade:'))
f=c*(9/5) +32
print ('temperature in Fahrenheit is:', f)
#Fahrenheit temperature into Centigrade
f1=float (input ('Enter temperature in Fahrenheit:'))
c1=5/9*(f1-32)
print ('temperature in Centigrade is:', c1)


'''OUTPUT
Enter temperature in Centigrade :35
temperature in Fahrenheit is: 95.0.
Enter temperature in Fahrenheit :95
temperature in Centigrade is: 35.0.'''