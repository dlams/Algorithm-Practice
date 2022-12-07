from sys import stdin, setrecursionlimit

setrecursionlimit(int(1e6))

n, m = map(int, stdin.readline().strip().split())
array = [ [] for _ in range(n) ]
for i in range(n):
    array[i] = list(map(int, stdin.readline().strip().split()))
#
maximum = 0
# tmp = 0

def dfs(x, y):
    global tmp, maximum
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if array[x][y]:
        array[x][y] = 0
        tmp += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        tmp = 0
        if dfs(i, j):
            res += 1
            maximum = max(maximum, tmp)

print(res)
print(maximum)
