from sys import stdin

t = int(input())
for _ in range(t):
    n = int(input())
    array = [list(map(int, input().split())), list(map(int, input().split()))]
    d = [[0] * (n + 2), [0] * (n + 2)]
    d[0][2:] = array[0]
    d[1][2:] = array[1]

    for idx in range(n):
        d[1][idx + 2] += max(d[0][idx:idx + 2])
        d[0][idx + 2] += max(d[1][idx:idx + 2])
    print(max(d[0][n + 1], d[1][n + 1]))
