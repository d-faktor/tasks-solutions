def sock_merchant(array):
    count_socks = {}
    pair = 0
    for i in array:
        if count_socks.get(i, 0) == 1:
            pair = pair + 1
            count_socks[i] = 0
        else:
            count_socks[i] = 1
            count_socks[i] = 1
    return pair


if __name__ == 'main__':
    str = input("Str: ")
    socks = list(map(int, str.split(',')))
    res = sock_merchant(socks)
    print(res)