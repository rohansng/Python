'''Write a function that returns the date obtained by incrementing date input in the format 
ddmmyyyy.'''

def date1(date):
    dd, mm, yyyy = date.split("/")
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)

    # Determine the maximum days in the given month
    if mm in [1, 3, 5, 7, 8, 10, 12]:
        max1 = 31
    elif mm in [4, 6, 9, 11]:
        max1 = 30
    elif (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
        max1 = 29  # Leap year
    else:
        max1 = 28

    # Validate the input date
    if mm < 1 or mm > 12:
        return 'Month is invalid'
    elif dd < 1 or dd > max1:
        return 'Date is invalid'

    # Increment the date
    if dd == max1 and mm < 12:  # End of month, but not end of year
        dd = 1
        mm += 1
    elif dd == 31 and mm == 12:  # End of year
        dd = 1
        mm = 1
        yyyy += 1
    else:  # Regular increment
        dd += 1

    print('Incremented date is:')
    return f"{dd:02d}/{mm:02d}/{yyyy}"

# Input the date and get the result
date = input('Enter the date (dd/mm/yyyy): ')
result = date1(date)
print(result)

'''
OUTPUT
enter the date:01/01/2023
incremented date is : 02/01/2023

enter the date: 31/01/2023
incremented date is : 01/02/2023

enter the date: 29/02/2023
incremented date is : 01/03/2024

enter the date: 31/12/2023
incremented date is : 01/01/2024

enter the date:29/02/2023
date is invalid

'''