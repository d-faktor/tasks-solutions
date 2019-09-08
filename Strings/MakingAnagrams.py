def make_anagram(a, b):
    diff = {}
    for i in a:
        diff[i] = diff.get(i, 0) + 1
    for i in b:
        diff[i] = diff.get(i, 0) - 1
    deletes = 0
    for value in diff.values():
        deletes = deletes + abs(value)
    return deletes


if __name__ == '__main__':
    string_a = input('Input string A: ')
    string_b = input('Input string B: ')
    result = make_anagram(string_a, string_b)
    print(result)
