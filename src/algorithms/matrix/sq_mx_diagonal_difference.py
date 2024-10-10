#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Sums of diagonals
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
        print(f'item is {i}/{n}')
        if matrix_item_is_valid(i, i, arr):
            d1 += arr[i][i]
        if matrix_item_is_valid(i, n-i-1, arr):
            d2 += arr[i][n - i - 1]
        print(f'{d1} {d2}')
         
    # Absolute difference between d1-d2
    return abs(d1 - d2)

def matrix_item_is_valid(i, j, arr) -> bool:
    if -100 <= arr[i][i] <= 100:
        return True
    return False

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
arr_1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
result = diagonalDifference(arr_1, 3)
print(f'result 1 is {result}')
# abs difference is 2
arr = [[11,2,4],[4,5,6],[10,8,-12]]
# abs difference is 15
result = diagonalDifference(arr, 3)
print(f'result 2 is {result}')