# bfs를 구현하기 위한 deque 로드
from collections import deque
# 빠른 입력을 위한 stdin 로드
from sys import stdin
input = stdin.readline

# 거리의 최대값 상수 설정
MAX_DISTANCE = int(1e5)
# n은 체스판 크기, m은 상대 말 갯수
n, m = map(int, input().split())

# 현재 나이트 위치
x, y = map(int, input().split())
x, y = x-1, y-1
# 적 말들 위치 저장
enemy = []

for _ in range(m):
    dx, dy = map(int, input().split())
    enemy.append((dx - 1, dy - 1))


# 나이트 이동 범위 설정
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

# 방문 처리 용 변수
visited = [[False for _ in range(n)] for __ in range(n)]

# n x n의 보드판 생성 및 도달 할 수 있는 거리 생성
board = [[MAX_DISTANCE for _ in range(n)] for __ in range(n)]
# bfs를 통해 움직일 수 있으면 거리 추가
queue = deque([(x, y)])
board[y][x] = 0
while queue:
    c_x, c_y = queue.popleft()
    if visited[c_y][c_x]:
        continue
    visited[c_y][c_x] = True
    for i in range(8):
        mx, my = c_x + dx[i], c_y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            board[my][mx] = min(board[my][mx], board[c_y][c_x] + 1)
            queue.append((mx, my))

# print(*board, sep="\n")

for ex, ey in enemy:
    print(board[ey][ex], end=" ")

