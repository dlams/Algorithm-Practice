from collections import deque
from sys import stdin

m, n, h = map(int, stdin.readline().strip().split())

graph = [ [] for i in range(h) ]
for floor in range(n * h):
    graph[floor // n].append(list(map(int, stdin.readline().strip().split())))


# 상 하 좌 후 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

def bfs():
    # 큐가 빌 때까지 실행
    while queue:
        x, y, z = queue.popleft()
        # 현재 위치에서 4방향으로 위치 확인
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 최대크기안에서 토마토가 0인 경우에만
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                # if graph[nx][ny] == 0 or graph[x][y] + 1 <= graph[nx][ny]:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nx, ny, nz))

for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 1:
                queue.append([i, j, k])
bfs()
res = 0
for i in graph:
    for j in i:
        for k in j:
            if not k:
                print(-1)
                exit(0)
            # print(k)
        res = max(res, max(j))
# print(graph)
print(res - 1)
