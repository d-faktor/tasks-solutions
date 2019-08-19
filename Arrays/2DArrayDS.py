import sys

def hourglass_sum(arr):
    sum = []
    for i in range(4):
        for j in range(4):
            val = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] \
                  + arr[i + 1][j + 1]  \
                  + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            sum.append(val)
    return max(sum)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        new_line = list(map(int, input("Line: ").rstrip().split()))
        if len(new_line) == 6:
            arr.append(new_line)
        else:
            print("It's wrong line(to much or to many elements)")
            sys.exit()
    result = hourglass_sum(arr)
    print(result)
