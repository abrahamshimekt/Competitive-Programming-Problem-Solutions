#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if (grades[i]//5 + 1)*5 - grades[i] >=3 or grades[i] <38:
            grades[i] = grades[i]
        elif (grades[i]//5 + 1)*5 - grades[i] <3:
            grades[i] = (grades[i]//5 + 1)*5
        
    return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()