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
    result_list = list()
    for i in range(rows_count):
        new_row = input().split()
        int_new_row = [int(x) for x in new_row]
        result_list.append(int_new_row[1:])
    return result_list


def merge_two_rows(list1, list2):
    result_list = list()
    i = 0
    j = 0
    list1_len = len(list1)
    list2_len = len(list2)
    while i < list1_len and j < list2_len:
        if list1[i] < list2[j]:
            result_list.append(list1[i])
            i += 1
        else:
            result_list.append(list2[j])
            j += 1
    if i < list1_len:
        result_list = result_list + list1[i:]
    if j < list2_len:
        result_list = result_list + list2[j:]
    return result_list


def merge_rows(input_list):
    length = len(input_list)
    while length > 1:
        new_list = list()
        while length > 1:
            new_list.append(merge_two_rows(input_list.pop(), input_list.pop()))
            length = len(input_list)
        if length == 1:
            new_list.append(input_list.pop())
        input_list = new_list
        length = len(input_list)
    return input_list[0]


if __name__ == '__main__':
    new_list = read_list()
    result = merge_rows(new_list)
    for value in result:
        print(value)
