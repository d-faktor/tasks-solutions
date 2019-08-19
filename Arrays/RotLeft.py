def rot_left(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    shift = int(input())
    array = list(map(int, input().rstrip().split()))
    result = rot_left(array, shift)
    print(result)

