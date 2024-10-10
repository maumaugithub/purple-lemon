# Binary Search in python


def recursiveBinarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return recursiveBinarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return recursiveBinarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [1000, 645, 4, 532, 6012, 127, 358, 999, 421]
# array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = recursiveBinarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")