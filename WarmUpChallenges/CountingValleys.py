#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    hight = 0
    valley_count = 0
    for i in s:
        if i == 'U':
            if hight == -1:
                valley_count = valley_count + 1
            hight = hight + 1
        else:
            hight = hight - 1

    return valley_count

if __name__ == '__main__':
    str = input("Str: ")
    num = int(input("Num: "))
    res = countingValleys(num, str)
    print(res)