"""
We need to generate correct brackets sequences with 2*n length
Input: n
Output: all correct brackets sequences
"""

def check_row(row):
    result = 0
    for value in row:
        result += value
        if result > 0:
            return 0
    if result == 0:
        return 1
    else:
        return 0


def print_brackets(input_list):
    for value in input_list:
        if value == -1:
            print('(', end='')
        else:
            print(')', end='')
    print()


def generate_all_variants(length, row, index):
    if index == length:
        if check_row(row):
            print_brackets(row)
        return

    new_row1 = row + [-1]
    generate_all_variants(length, new_row1, index + 1)

    new_row2 = row + [1]
    generate_all_variants(length, new_row2, index + 1)


if __name__ == '__main__':
    input_length = int(input())
    input_row = []
    generate_all_variants(input_length*2, input_row, 0)
