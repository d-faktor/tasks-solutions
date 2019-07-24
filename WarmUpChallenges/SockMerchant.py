#!/bin/python3

import os

# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    count_socks = {}
    pair = 0
    for i in ar:
        if count_socks.get(i, 0) == 1:
            pair = pair + 1
            count_socks[i] = 0
        else:
            count_socks[i] = 1

    return pair


if __name__ == 'main__':
    str = input("Str: ")
    socks = list(map(int, str.split(',')))
    num = int(input("Num: "))
    res = sock_merchant(num, socks)
    print(res)