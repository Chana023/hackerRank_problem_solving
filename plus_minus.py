# iven an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

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
    # Write your code here
    negative_count = 0
    positive_count = 0
    zero_count = 0

    for value in arr:
        if value > 0:
            positive_count = positive_count + 1       
        elif value < 0:
            negative_count = negative_count + 1       
        elif value == 0:
            zero_count = zero_count + 1

    print(f'{(positive_count/len(arr)):.6f}')
    print(f'{(negative_count/len(arr)):.6f}')
    print(f'{(zero_count/len(arr)):.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
