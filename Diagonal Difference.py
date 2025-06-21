#Source: 
#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

#date: 2026-06-20
#solved: no

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
    length = n
    
    for i in range(length):
        l_index = arr[i][i]
        r_index = arr[i][i-1]
    print(l_index)
    print(r_index)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

