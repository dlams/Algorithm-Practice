from sys import setrecursionlimit

setrecursionlimit(int(1e9))

n, k = map(int, input().split())
d = [0] * 100_001

def dfs(x: int):
    if d[x] == 0:
        d[x] = min(d[x],)

print(dfs(k))