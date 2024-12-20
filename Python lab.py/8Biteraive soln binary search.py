'''Develop an iterative solution for binary search'''
list1 = [2, 3, 4, 10, 40]  # List of elements
elem_to_search = 40         # Element to search
low = 0                     # Starting index
high = len(list1) - 1       # Ending index

# Binary search loop
while low <= high:
    mid = (high + low) // 2  # Calculate the middle index

    # Check if the element is at the middle index
    if list1[mid] == elem_to_search:
        print('Element present at index', mid)
        break
    # If the element is greater, ignore the left half
    elif list1[mid] < elem_to_search:
        low = mid + 1
    # If the element is smaller, ignore the right half
    else:
        high = mid - 1
else:
    # If the element is not found
    print('Element not found')


'''
OUTPUT
Element present at index 4
'''