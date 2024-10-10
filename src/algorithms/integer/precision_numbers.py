#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size = len(arr)
    # Setting array size constraints
    if 0 <= size <= 100:
        arr_i = list(arr)
        # Obtain positive, negative and zero elements
        zero_nums = [v for i, v in enumerate(arr_i) if v == 0]
        positive_nums = [v for i, v in enumerate(arr_i) if 0 < v <= 100]
        negative_nums = [v for i, v in enumerate(arr_i) if -100 <= v < 0]
        # Calculate proportions
        proportions = [len(positive_nums)/size, len(negative_nums)/size, len(zero_nums)/size]
        # Print formatted proportions
        [print(format(p, ".6f")) for p in proportions]
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
