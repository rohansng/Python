'''Input N numbers and create a list. Develop a program to print mean, variance and 
standard deviation of the numbers with appropriate messages.'''

import math

# Initialize an empty list
list1 = []

# Input the size of the list
print('Enter size of the list:')
num = int(input())

# Input elements into the list
print('Enter the elements into the list:')
for i in range(num):
    x = int(input())
    list1.append(x)

# Display the elements of the list
print('The elements in the list are:', list1)

# Calculate mean, variance, and standard deviation
n = len(list1)
numerator_total = 0
sum_elements = 0

# Calculate the sum of the elements
for k in list1:
    sum_elements += k

# Calculate the mean
mean = sum_elements / n

# Calculate the variance
for x in list1:
    var = (x - mean) ** 2
    numerator_total += var

variance = numerator_total / (n - 1)  # Variance (sample)
std_dev = math.sqrt(variance)  # Standard deviation

# Display the results
print('Mean =', mean)
print('Variance =', variance)
print('Standard Deviation =', std_dev)

'''OUTPUT
enter size of list
4
enter the elements into the list
2
3
4
5
The elements in the list are [2, 3, 4, 5]
Mean= 3.5
Variance= 1.6666666666666667
'''

def calc_average(lst):
    return sum(lst) / len(lst)

def calc_variance(lst, mean_value):
    ans = sum((i - mean_value) ** 2 for i in lst) / (len(lst) - 1)  # Replace wrong dash with subtraction operator
    return ans

def calc_stdev(variance):
    res = variance ** 0.5
    return res

lst = [1, 2, 3, 4, 5, 6]
mean_value = calc_average(lst)
print("Mean of the list is", mean_value)

variance = calc_variance(lst, mean_value)
print("Variance of the list is", variance)

standard_deviation = calc_stdev(variance)
print("Standard deviation of the list is", standard_deviation)


'''OUTPUT
Mean of the list is 3.5
Variance of the list is 3.5
Standard deviation of the list is 1.8708286933869707
'''
