from sys import stdin, setrecursionlimit

setrecursionlimit(int(1e6))

n = int(stdin.readline())
graph = [
    [i for i in stdin.readline().strip()] for _ in range(n)
]
visited = [False] * pow(n, 2)

def dfs(x, y, color):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 기존 색인지 체크
    if visited[x * n + y]:
        return False
    if graph[x][y] in color:
        visited[x * n + y] = True
        dfs(x + 1, y, color)
        dfs(x - 1, y, color)
        dfs(x, y + 1, color)
        dfs(x, y - 1, color)
        return True
    return False

res_normal = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, graph[i][j]):
            res_normal += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

res = 0
visited = [False] * pow(n, 2)
for i in range(n):
    for j in range(n):
        if dfs(i, j, graph[i][j]):
            res += 1

print(res_normal, res)
# print(len(res))
