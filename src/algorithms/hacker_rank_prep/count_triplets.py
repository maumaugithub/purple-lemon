#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    print(r)

    possible_dict = {}
    possible_list = []
    dups = Counter(arr)
    print(f'{len(dups.items())} : keys {range(len(dups.keys()))} : {dups}')
    
    if len(dups.items())<3:
        return 0

    for i in iter(dups.keys()):
        print(f'i is {i} : v is {dups[i]}')
        
        triplet = (arr[idx],arr[idx+1],arr[idx+2])
        t = dups.get(i, 0)
        print(t)
        for ts in range(1,t):
            possible_list.append(triplet)
    
    
    print(possible_list)
    return len(possible_list)

def do_add(item_list, l):
    l.append(item_list)

    # poss = permutations(arr, r)
    # print(list(poss))
    # possible = list(permutations(set(arr), r))
    # 
    # 
#  print(dups[arr[i+1]])
#             j = i + dups[arr[i+1]]
#             if arr[i+1] < arr[j]:
#                 triplet = (arr[i], arr[i+1], arr[j]) 
#                 print(f'triplet {triplet}')
#                 possible_list.append(triplet)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nr = input().rstrip().split()

#     n = int(nr[0])

#     r = int(nr[1])

#     arr = list(map(int, input().rstrip().split()))

#     ans = countTriplets(arr, r)

#     fptr.write(str(ans) + '\n')

#     fptr.close()
# r = 5
# 1 5 5 25 125 # 4

r1 = 2
arr1 = [1,2,2,4] #2
result1 = countTriplets(arr1, r1)

r2 = 3
arr2 = [1, 3, 9, 9, 27, 81] #6

result2 = countTriplets(arr2, r2)


# def countTriplets(arr, r):
    
#     if r == 1:
#         triples = 0
#         n_dict = list_to_dict(arr)
#         for n in n_dict:
#             triples += math.comb(n_dict[n], 3)
#         return triples

#     n_dict = {}
#     pair_dict = {}
#     triple_dict = {}
    
#     for n in arr:
#         if n in n_dict:
#             n_dict[n] += 1
#         else:
#             n_dict[n] = 1
#         m = n // r
#         if m in n_dict:
#             if (m, n) in pair_dict:
#                 pair_dict[(m, n)] += n_dict[m]
#             else:
#                 pair_dict[(m, n)] = n_dict[m]
#         l = m // r
#         if (l, m) in pair_dict:
#             if (l, m, n) in triple_dict:
#                 triple_dict[(l, m, n)] += pair_dict[(l, m)]
#             else:
#                 triple_dict[(l, m, n)] = pair_dict[(l, m)]
    
#     return sum(triple_dict.values())