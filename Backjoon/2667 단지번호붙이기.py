import sys

n = int(sys.stdin.readline().strip())
graph = [ [ int(i) for i in sys.stdin.readline().strip() ] for _ in range(n) ]


def dfs(x, y):
    result = 0
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        result += dfs(x + 1, y)
        result += dfs(x - 1, y)
        result += dfs(x, y + 1)
        result += dfs(x, y - 1)
        return result + 1
    return 0

result = []
for i in range(n):
    for j in range(n):
        tmp = dfs(i, j)
        if tmp:
            result.append(tmp)
print(len(result))
result.sort()
print(*result, sep="\n")
