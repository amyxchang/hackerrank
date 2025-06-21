#Source: 
#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

#date: 2026-06-20
#solved: yes

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    ascore = 0
    bscore = 0

    length = len(a)
    
    for i in range(length):
        if a[i] > b[i]:
            ascore+=1
        elif a[i] < b[i]:
            bscore+=1
        
    return [ascore, bscore]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

print(result)
