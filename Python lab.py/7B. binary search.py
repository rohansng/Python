'''Develop a recursive function to perform binary search on a sorted list of names. The 
function returns the position of a name passed as argument to the function.'''

def binary_search(arr, low, high, elem_to_search):
    if high >= low:
        mid = (low + high) // 2
        if elem_to_search == arr[mid]:
            return mid
        elif elem_to_search < arr[mid]:
            return binary_search(arr, low, mid - 1, elem_to_search)
        else:
            return binary_search(arr, mid + 1, high, elem_to_search)
    else:
        return -1

list1 = ["Ram", "Sita", "Veena"]
low = 0
high = len(list1) - 1
elem_to_search = "Sita"
result = binary_search(list1, low, high, elem_to_search)
if result == -1:
    print("Element not found!")
else:
    print("Element found at index", result)

'''
OUTPUT
Element found at index 1
'''