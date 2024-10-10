#!/bin/python3

import math
import os
import random
import re
import sys
import time

# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s) -> str:
    print(s[0:2])
    if "AM" in s and s[0:2] == "12":
        return "00" + s[2:-2]
    elif "AM" in s and 0 <= int(s[0:2]) < 12:
        return s[0:-2]
    elif "PM" in s and s[0:2] == "12":
        return s[0:-2]
    elif "PM" in s and 0 <= int(s[0:2]) < 12:
        adjusted_time = 12 + int(s[0:2])
        return str(adjusted_time) + s[2:-2]
        

#if __name__ == '__main__':
#fptr = open(os.environ['OUTPUT_PATH'], 'w')

# s = '12:00:00AM' # is 00:00:00 on a 24-hour clock
# s = '12:00:01AM'
# s = '15:00:01AM'
# s = '12:00:00PM'
s = '11:00:01PM'
# s = "10:10:00PM"
# s = "07:05:45PM"

result = timeConversion(s)
print(f'The result is {result}')

#fptr.write(result + '\n')
#fptr.close()
