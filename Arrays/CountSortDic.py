"""
We need to merge k sorted arrays:
Input:
k
len(a1) a11 a12 ... a1n
. . .
len(ak) ak1 ak2 ... akn

"""


def read_dict():
    rows_count = int(input())
    result_dict = {str(x): 0 for x in range(100)}
    for i in range(rows_count):
        new_row = input().split()
        size = int(new_row[0])
        if size > 0:
            for index in range(1, size + 1):
                result_dict[new_row[index]] += 1
    return result_dict


def print_result(result_dict):
    for i in range(100):
        char = str(i)
        print(' '.join([char] * result_dict[char]))


if __name__ == '__main__':
    new_dict = read_dict()
    print_result(new_dict)
