"""
We need to generate correct brackets sequences with 2*n length
Input: n
Output: all correct brackets sequences
"""


def generate_correct_sequence(n, open_brackets_count, close_brackets_count, current_string):
    if open_brackets_count + close_brackets_count == 2*n:
        print(current_string)
        return
    if open_brackets_count < n:
        generate_correct_sequence(n, open_brackets_count + 1, close_brackets_count, current_string + '(')
    if close_brackets_count < open_brackets_count:
        generate_correct_sequence(n, open_brackets_count, close_brackets_count + 1, current_string + ')')


if __name__ == '__main__':
    length = int(input())
    generate_correct_sequence(length, 0, 0, "")
