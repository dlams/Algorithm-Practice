from collections import deque

# 상 하 좌 우 좌상단 우상단 좌하단 우하단
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    while queue:
        nx, ny = queue.popleft()
        for i in range(8):
            a = nx + dx[i]
            b = ny + dy[i]
            if 0 <= a < N and 0 <= b < M and graph[a][b] == 1:
                graph[a][b] = 0
                queue.append([a, b])

while 1:
    M, N = map(int, input().split())
    if M+N == 0:
        break
    res = 0
    graph = [
        list(map(int, input().split())) for _ in range(N)
    ]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                res += 1

    print(res)