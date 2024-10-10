#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         result = towerBreakers(n, m)

#         fptr.write(str(result) + '\n')

#     fptr.close()

# n = 2
# m = 5

# n = 1 m = 7 -> 1
# n = 3, m = 7 -> 1
# n = 2,  m = 6 -> 2
# n = 2, m = 2 -> 2
# n = 1, m = 4 -> 1
# n = 100000 m = 1 -> 2
# n = 374625 m = 796723 # ->1

# 950929 183477 1

# 732159 779867 1

# n = 598794 m = 596985  #->2

# 156054 445934 2

# n = 156030 m = 99998 # -> 2

n = 58097 
m = 459353 #1

# 866372 333784 2

result = towerBreakers(n, m)

# if m == 1:
#         return 2
#     elif n == 1:
#         return 1
#     elif 1< m <= 1000000 and 1 < n <= 1000000:
#         if n % 2 == 0 or m % 2 == 0:
#             return 2
#         else:
#             return 1