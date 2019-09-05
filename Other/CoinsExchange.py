def minimum_element(input_list):
    positive_list = [value for value in input_list if value >= 0]
    if len(positive_list) == 0:
        return -1
    else:
        return min(positive_list)


def find_best_exchange(exchange_values, number, already_calculated_values):
    if number in exchange_values:
        return 1
    if number < 0:
        return -1
    if already_calculated_values.get(number, 0) != 0:
        return already_calculated_values[number]

    exchange_options = list()
    for value in exchange_values:
        new_value = find_best_exchange(exchange_values, number - value, already_calculated_values)
        exchange_options.append(new_value)
    exchange_count = minimum_element(exchange_options)

    if exchange_count < 0:
        result_value = -1
    else:
        result_value = 1 + exchange_count

    already_calculated_values[number] = result_value
    return result_value


if __name__ == '__main__':
    input_exchange_values = input("Input coins for exchange:")
    exchange_values = [int(value) for value in input_exchange_values.split(',')]
    number = int(input("Input number:"))
    already_calculated_values = dict()
    result = find_best_exchange(exchange_values, number, already_calculated_values)
    if result < 0:
        print("We can't do it")
    else:
        print(result)
        print(already_calculated_values)
