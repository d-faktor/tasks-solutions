def jumping_on_clouds(num, clouds):
    i = 0
    steps = 0
    while i < num:
        if i + 2 < num and clouds[i + 2] == 0:
            steps = steps + 1
            i = i + 2
        elif i + 1 < num and clouds[i + 1] == 0:
            steps = steps + 1
            i = i + 1
        else:
            break
    return steps


if __name__ == 'main__':
    str = input("Str: ")
    clouds = list(map(int, str.split()))
    num = int(input("Num: "))
    res = jumping_on_clouds(num, clouds)
    print(res)