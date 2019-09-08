import math


def is_valid_string(input_string):
    character_dict = dict()
    for character in input_string:
        character_dict[character] = character_dict.get(character, 0) + 1

    value_list = list(character_dict.values())
    min_value = min(value_list)
    max_value = max(value_list)

    if min_value == max_value:
        return 'YES'
    if min_value - 1 != 0 and max_value - min_value > 1:
        return 'NO'

    min_count = 0
    max_count = 0
    diff_count = 0
    for value in value_list:
        if min_value == value:
            min_count += 1
        elif max_value == value:
            max_count += 1
        else:
            return 'NO'
    if (min_count == 1 and min_value - 1 == 0) or (max_count == 1 and max_value - min_value == 1):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    input_string = input('Input string: ')
    result = is_valid_string(input_string)
    print(result)
