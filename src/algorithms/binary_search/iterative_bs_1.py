# Binary Search in python
# Assumes an ordered list as input


def iterativeBinarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2
        print(f'mid is : {mid}')

        # If x found at mid, then return it
        if array[mid] == x:
            return mid

        # narrow left half
        elif array[mid] < x:
            low = mid + 1

        # narrow right half
        else:
            high = mid - 1

    else:
        return -1
    

def ascIterativeBinarySearch(array, x, high, hint: int = 0):
    low = 0

    if low <= high and hint <= high:
        if array[hint] == x:
            print(f'Hint index {hint} value is x')
            return hint
        elif array[hint] < x:
            print(f'Hint index {hint} value is smaller than x')
            return iterativeBinarySearch(array, x, hint + 1, high)
        else:
            print(f'Hint index {hint} value is bigger than x')
            return ascIterativeBinarySearch(array, x, hint - 1, hint - 1)


# array = [3, 4, 5, 6, 7, 8, 9]
# array = [1, 4, 532, 612, 823, 1358, 1999, 3421]
array = [-1000, -645, 4, 532, 612, 927, 1358, 1999, 2321, 3421]
x = 4

result = iterativeBinarySearch(array, x, 0, len(array)-1)
# result = ascIterativeBinarySearch(array, x, len(array)-1, 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")