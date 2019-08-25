def check_magazine(magazine, note):

    magazine_dic = dict()
    for word in magazine:
        magazine_dic[word] = magazine_dic.get(word, 0) + 1
    for word in note:
        if magazine_dic.get(word, 0) == 0:
            return 'No'
        else:
            magazine_dic[word] = magazine_dic[word] - 1
    return 'Yes'


if __name__ == '__main__':
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    result = check_magazine(magazine, note)
    print(result)

