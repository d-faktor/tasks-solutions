#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries, array):
    result = array
    for i in range((queries[0] - 1), queries[1], 1):
        result[i] = result[i] + queries[2]
    return result

if __name__ == '__main__':
    fh = open('Queries.txt', 'r')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    result = [0] * n

    for line in fh:
        queries = list(map(int, line.rstrip().split()))
        print(queries)
        result = arrayManipulation(n, queries, result)

    ##fptr.write(str(max(result)) + '\n')
    print(max(result))
    ##fptr.close()
