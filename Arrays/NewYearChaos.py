#!/bin/python3
# Complete the minimumBribes function below.
def minimumBribes(q, n):
    bribes_cnt = 0
    q = [value - 1 for value in q]
    for i, value in enumerate(q):
        if value - i > 2:
            bribes_cnt = -1
            break
        else:
            for j in range(max(value - 1, 0), i, 1):
                if value < q[j]:
                    bribes_cnt = bribes_cnt + 1
    return bribes_cnt

if __name__ == '__main__':
    t = int(input())
    res = []
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        res.append(minimumBribes(q, n))

    for bribe in res:
        if bribe == -1:
            print("Too chaotic")
        else:
            print(bribe)
