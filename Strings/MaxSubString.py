def find_max_substring_index(input_string):
    max_length = 0
    current_length = 1
    max_index = 0
    current_index = 0
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            current_index = i
            current_length = 0
        current_length += 1
        if max_length < current_length:
            max_length = current_length
            max_index = current_index
    return max_index


if __name__ == '__main__':
    input_string = input("String: ")
    result = find_max_substring_index(input_string)
    print(result)