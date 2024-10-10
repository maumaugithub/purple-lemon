#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    if len(arr) == 5:
        size = len(arr)-1
        print(f'Calculating {size} / {len(arr)}')
        arr.sort()
        print(arr)
        print(10**9)
        min_elems = [v for i, v in enumerate(list(arr)) if i + 1 <= size and 1 <= v <= 10**9]
        max_elems = [v for i, v in enumerate(list(arr)) if 1 <= i <= len(arr) and 1 <= v <= 10**9]
        print(min_elems)
        print(max_elems)
        mins_total = sum(list(min_elems))
        print()
        maxs_total = sum(list(max_elems))
        print(f'{mins_total} {maxs_total}')
    

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

# sample = [1,3,5,7,9]
# sample = '1 2 3 4 5'
sample = '10 1000000000 1 1 1000000001'
arr = list(map(int, sample.rstrip().split()))

miniMaxSum(arr)