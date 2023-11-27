# Given a square matrix, calculate the absolute difference between the sums of its diagonals

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

def diagonalDifference(arr):
    # Write your code here
    ltr = 0
    rtl = 0
    for value in range(len(arr)):
        ltr = ltr + arr[value][value]
        rtl = rtl + arr[value][((len(arr))-1)-value]

    return abs(ltr-rtl)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

