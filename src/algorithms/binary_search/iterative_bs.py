# Binary Search in python
# Assumes an ordered list as input

    
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    steps = 0
 
    while low <= high:
        steps = steps + 1
        mid = (high + low) // 2
        # mid = low + (high - low)//2
        print(f'mid is : {mid}')
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid, steps
 
    # If we reach here, then the element was not present
    return -1
 

# array = [3, 4, 5, 6, 7, 8, 9]
# array = [1, 4, 532, 612, 823, 1358, 1999, 3421]
# array = [-1000, -645, 4, 532, 612, 927, 1358, 1999, 2321, 3421]
# x = 4
import numpy as np

# create 1000 equally spaced points between -10 and 10
array = np.linspace(-10, 10, 1000)

x = array[300]

result, steps = binary_search(array, x)
# result = ascIterativeBinarySearch(array, x, len(array)-1, 1)

if result != -1:
    print(f'Element x = {x} is present at index {str(result)} in {steps} steps for {len(array)} elements')
else:
    print("Not found")