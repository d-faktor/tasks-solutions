"""
Find the longest sequence of 1
Input:
l = Length
a1
a2
.
.
al
"""


def find_longest_sequence():
    max_length = 0
    current_length = 0
    length = int(input())
    for i in range(length):
        value = int(input())
        if value == 1:
            current_length += 1
        else:
            current_length = 0
        if max_length < current_length:
            max_length = current_length

    print(max_length)


if __name__ == '__main__':
    find_longest_sequence()

