def counting_valleys(n, s):
    height = 0
    valley_count = 0
    for i in s:
        if i == 'U':
            if height == -1:
                valley_count = valley_count + 1
            height = height + 1
        else:
            height = height - 1
    return valley_count


if __name__ == '__main__':
    str = input("Str: ")
    num = int(input("Num: "))
    res = counting_valleys(num, str)
    print(res)