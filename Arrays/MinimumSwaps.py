def minimum_swaps(arr):
        swaps_cnt = 0
        i = 0
        n = len(arr)
        q = [value - 1 for value in arr]
        while i < n:
            if q[i] - i == 0:
                i = i + 1
                continue
            else:
                x = q[i]
                q[i] = q[x]
                q[x] = x
                swaps_cnt = swaps_cnt + 1

        return swaps_cnt


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimum_swaps(arr)
    print(res)
