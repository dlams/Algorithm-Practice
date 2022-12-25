from collections import deque
from sys import maxsize, stdin
NOT SOLVED

input = stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[maxsize] * m for _ in range(n)]

baby_shark = []
for x in range(n):
    for y in range(m):
        if graph[x][y]:
            baby_shark.append((y, x))

# 상 하 좌 우 좌상단 우상단 좌하단 우하단
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def dfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y)])
    distance = 1
    while queue:
        qx, qy = queue.popleft()
        for i in range(8):
            if 0 <= qx + dx[i] < n and 0 <= qy + dy[i] < m:
                if visited[qx + dx[i]][qy + dy[i]]:
                    continue
                dist[qx + dx[i]][qy + dy[i]] = min(dist[qx + dx[i]][qy + dy[i]], distance)
                queue.append((qx + dx[i], qy + dy[i]))
                visited[qx + dx[i]][qy + dy[i]] = True
        distance += 1

for y, x in baby_shark:
    dfs(x, y)

res = 0
for y, x in baby_shark:
    res = max(res, dist[x][y])

print(res)