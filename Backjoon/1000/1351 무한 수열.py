from collections import defaultdict
from sys import stdin

input = stdin.readline

def dfs(n: int):
    if n < 0:
        return 1
    if data[n] != 0:
        return data[n]
    data[n] = dfs(n // p - x) + dfs(n // q - y)
    return data[n]


n, p, q, x, y = map(int, input().split())
data = defaultdict(int)
data[0] = 1

print(dfs(n))
