#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def 
def superDigit(n, k):
    
    while n > 9:
        sum_digit = 0
        while n > 0:
            sum_digit +=  n%10
            n //=10
        n = sum_digit
        
    while k > 9:
        sum_digit = 0
        while k > 0:
            sum_digit +=  k%10
            k//=10
        k = sum_digit
    super_digit = k*n
    
    while super_digit>9:
        sum_digit = 0
        while super_digit>0:
            sum_digit += super_digit%10
            super_digit//=10
        super_digit = sum_digit
    return super_digit
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
