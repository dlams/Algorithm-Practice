from collections import deque

N, M = map(int, input().split())
graph = [
    [int(i) for i in input()] for _ in range(N)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 실행
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로에서 벗어난 경우 제외
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0: # 원래 x, y로 되었었는데 그게 맞나..?
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N - 1][M - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))

# 5 DFS BFS 6
# 101010
# 111111
# 000001
# 111111
# 111111

#  3 그리디,  0,  5 DFS BFS,  0,  7,  0
#  2,  3 그리디,  4 구현,  5 DFS BFS,  6,  7
#  0,  0,  0,  0,  0,  8
# 14, 13, 12, 11, 10,  9
# 15, 14, 13, 12, 11, 10
