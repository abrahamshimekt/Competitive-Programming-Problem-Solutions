#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    nums = [0]*n
    for q in queries:
        nums[q[0]-1] += q[2]
        if q[1] < n:
            nums[q[1]] -= q[2]
        
    prefix_sum = nums[0]
    max_sum = nums[0]
    for index in range(1,n):
        prefix_sum += nums[index]
        max_sum = max(max_sum,prefix_sum)
    return max_sum
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
