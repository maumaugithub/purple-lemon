#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# 
# Constraints

# It is guaranteed that
# is an odd number and that there is one unique element.
# , where .

def lonelyinteger(a):
    size = len(a)
    if size == 1:
        return a[0]
    elif 1 < size < 100:
        x = 0
    
        # Apply XOR function if it meets constraint
        for i in a:
            if 0 <= i <= 100:
                x = x ^ i
    
        return x

    #  a = sorted(a)
    # size = len(a)
    # last_item = size - 1
    # if size == 1:
    #     return a[0]
    # elif 1 < size < 100:
    #     if 0 <= a[last_item-1] < a[last_item] <= 100:
    #         return a[last_item]
    #     return None
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     result = lonelyinteger(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()


test_arr = [0,0,1,2,3,4,3,2,1,4,100,101,102,101,102]

n = len(test_arr)

print(f'array size {n}: {test_arr}')

result = lonelyinteger(test_arr)