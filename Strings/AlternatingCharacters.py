def alternating_characters(s):
    length = len(s)
    deletes = 0
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            deletes = deletes + 1
    return deletes


if __name__ == '__main__':
    quantity = int(input())
    for q_itr in range(quantity):
        input_string = input()
        result = alternating_characters(input_string)
        print(result)


