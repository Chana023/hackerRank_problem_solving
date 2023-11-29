# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
import time

def timeConversion(s):
    # Write your code here
    t = time.strptime(s, "%I:%M:%S%p")
    t1 = time.strftime("%H:%M:%S", t)
    time_var = str(t1)

    print(time_var)

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

