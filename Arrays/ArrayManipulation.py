def array_manipulation(n, queries, array):
    result = array
    for i in range((queries[0] - 1), queries[1], 1):
        result[i] = result[i] + queries[2]
    return result

if __name__ == '__main__':
    fh = open('Queries.txt', 'r')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    result = [0] * n

    for line in fh:
        queries = list(map(int, line.rstrip().split()))
        result = array_manipulation(n, queries, result)

    print(max(result))

