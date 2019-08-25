def two_strings(s1, s2):

    s1_length = len(s1)
    s2_length = len(s2)
    min_length = min(s1_length, s2_length)
    letter_dict = dict()

    for i in range(min_length):
        if letter_dict.get(s1[i], 0) == 0:
            letter_dict[s1[i]] = 1
        elif letter_dict.get(s1[i], 0) == 2:
            return 'YES'
        if letter_dict.get(s2[i], 0) == 0:
            letter_dict[s2[i]] = 2
        elif letter_dict.get(s2[i], 0) == 1:
            return 'YES'

    if s1_length < s2_length:
        for i in range(s1_length - 1, s2_length):
            if letter_dict.get(s2[i], 0) == 1:
                return 'YES'
    else:
        for i in range(s2_length - 1, s1_length):
            if letter_dict.get(s1[i], 0) == 2:
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = two_strings(s1, s2)
        print(result)
