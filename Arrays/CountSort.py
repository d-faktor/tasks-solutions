"""
We need to merge k sorted arrays:
Input:
k
len(a1) a11 a12 ... a1n
. . .
len(ak) ak1 ak2 ... akn

"""


def read_list():
    rows_count = int(input())
    result_list = [0] * 100
    for i in range(rows_count):
        new_row = input().split()
        new_row = (int(x) for x in new_row[1:])
        for value in new_row:
            result_list[value] += 1
    return result_list


def print_result(result_list):
    for index, value in enumerate(result_list):
        for count in range(value):
            print(index, end=' ')


if __name__ == '__main__':
    new_list = read_list()
    print_result(new_list)
