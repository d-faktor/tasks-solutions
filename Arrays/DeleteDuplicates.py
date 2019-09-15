"""
We need to delete duplicates
Input:
n = length
a1
a2
.
.
an
Output:
a_unic1
a_unic2
.
.
"""


def delete_duplicates():
    length = int(input())
    value = int(input())
    result = list()
    for i in range(length-1):
        prev_value = value
        value = int(input())
        if prev_value != value:
            result.append(prev_value)
    result.append(value)
    for value in result:
        print(value)


if __name__ == '__main__':
    delete_duplicates()
