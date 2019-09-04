def minimum_element(input_list):
    positive_list = [value for value in input_list if value >= 0]
    if len(positive_list) == 0:
        return -1
    else:
        return min(positive_list)


def find_best_exchange(exchange_values, number):
    if number in exchange_values:
        return 1
    if number < 0:
        return -1
    exchange_options = list(map(lambda value: find_best_exchange(exchange_values, number - value), exchange_values))
    exchange_count = minimum_element(exchange_options)
    if exchange_count < 0:
        return -1
    return 1 + exchange_count


if __name__ == '__main__':
    exchange_values = [5]
    number = 7
    result = find_best_exchange(exchange_values, number)
    if result < 0:
        print("We can't do it")
    else:
        print(result)
