#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(queries):
    sum = 0
    max_value = 0
    operations = queries
    operations.sort()
    for operation in operations:
        sum = sum + operation[1]
        if sum > max_value:
            max_value = sum
    return max_value

if __name__ == '__main__':
    fh = open('Queries.txt', 'r')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    result = [0] * n

    for line in fh:
        query = list(map(int, line.rstrip().split()))
        queries.append((int(query[0]), int(query[2])))
        queries.append((int(query[1]) + 1, -1 * int(query[2])))

result = arrayManipulation(queries)
print(result)
    ##fptr.write(str(max(result)) + '\n')
   ## print(max(result))
    ##fptr.close()
