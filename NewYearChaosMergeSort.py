#!/bin/python3
# Complete the minimumBribes function below.

def mergeArray(array1, array2, count):
    print("Merge begin",array1, array2, count)
    len1 = len(array1)
    len2 = len(array2)
    bribe_count = count
    result = []
    i = 0
    j = 0
    while (i < len1 and j < len2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i = i + 1
        else:
            result.append((array2[j]))
            bribe_count = bribe_count + 1
            j = j + 1
    print("Merge end",result, bribe_count)
    return (result, bribe_count)

def minimumBribes(array, count):
    print("Begin", array, count)
    length = len(array)
    sort_list = array
    if length == 1:
        return (array, count)

    middle = length//2
    res1 = minimumBribes(sort_list[:middle], count)
    res2 = minimumBribes(sort_list[middle:], count)

    array1 = res1[0]
    array2 = res2[0]
    result = []
    res = mergeArray(array1, array2, res1[1] + res2[1])
    print("End", res)
    return res

if __name__ == '__main__':
    t = int(input())
    res = []
    for t_itr in range(t):
        n = int(input())
        c = 0
        q = list(map(int, input().rstrip().split()))

        res.append(minimumBribes(q, c))

    for bribe in res:
        if bribe == -1:
            print("Too chaotic")
        else:
            print(bribe)
