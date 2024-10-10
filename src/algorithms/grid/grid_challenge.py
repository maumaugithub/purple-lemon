#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import pairwise
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # This just compares the columns content assumes rows already sorted
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # coords = [' '.join(s).split() for k, s in enumerate(grid)]
    # col_size = len(coords[0])
    # print(coords)
    # if not all(alphabet.find(coords[i][j]) <= alphabet.find(coords[i+1][j]) for i in range(n-1) for j in range(col_size-1)):
    #     return "NO"
    # return "YES"

    # this creates a coordinates map for the grid
    # coords = [(k, s[i]) for k, s in enumerate(grid) for i in range(n) if grid[k]<=grid[n-1]]
    # print(f'{coords} ')

    #  This compares across both row and columns
    # if all(coords[i][j] <= coords[i][j+1] and coords[i][j] <= coords[i+1][j] for i in range(n-1) for j in range(col_size-1)):
    #     return "YES"
    # return "NO"

    for s1, s2 in pairwise(grid):
        print(f'{s1} {s2}')
        if not all(i <= j for i, j in zip(sorted(s1), sorted(s2))):
            return "NO"
    return "YES"

# This block of code is the main part of the script. It reads input from the user, processes it using
# the `gridChallenge` function, and writes the result to an output file specified by
# `os.environ['OUTPUT_PATH']`. Here's a breakdown of what each part does:
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         grid = []

#         for _ in range(n):
#             grid_item = input()
#             grid.append(grid_item)

#         result = gridChallenge(grid)

#         fptr.write(result + '\n')

#     fptr.close()

# n = 3
# grid = ['abcd', 'adee', 'efgz']
# a b c
# a d e
# e f g

# n = 5
# grid = ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']
# eabcd

# fghij

# olkmn

# trpqs

# xywuv


# n = 5
# ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# fghij
# olmkn
# trpqs
# xywuv

# given
# 3

# hcd

# awc

# shm

# 3

# sur

# eyy

# gxy

# 3

# nyx

# ynx

# xyt

# 4

# vpvv

# pvvv

# vzzp

# zzyy

n = 4
grid = ['vpvv', 'pvvv', 'vzzp', 'zzyy']
# expected
    # NO

    # NO

    # YES

    # YES
    
result = gridChallenge(grid)