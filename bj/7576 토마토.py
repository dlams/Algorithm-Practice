from collections import deque
from sys import stdin

M, N = map(int, stdin.readline().strip().split())
graph = [
    list(map(int, stdin.readline().strip().split())) for _ in range(N)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():
    # 큐가 빌 때까지 실행
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 최대크기안에서 토마토가 0인 경우에만
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            # if graph[nx][ny] == 0 or graph[x][y] + 1 <= graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])
bfs()
res = 0
for i in graph:
    for j in i:
        if not j:
            print(-1)
            exit(0)

    res = max(res, max(i))
print(res - 1)
