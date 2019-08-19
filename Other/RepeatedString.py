def repeated_string(s, n):
    letter_amount = s.count('a')
    s_length = len(s)
    repeated_amount = n // s_length
    rest_amount = s[:n % s_length].count('a')
    return repeated_amount*letter_amount + rest_amount


if __name__ == 'main__':
    str = input("Str: ")
    num = int(input("Num: "))
    res = repeated_string(str, num)
    print(res)