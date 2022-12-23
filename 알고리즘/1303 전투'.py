from sys import stdin
from collections import deque

# input = stdin.readline

n, m = map(int, input().split())
graph = [[c for c in input()] for _ in range(m)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, c):
    queue = deque([(x, y)])
    color = c
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            rx, ry = px + dx[i], py + dy[i]
            if 0 <= rx < n and 0 <= ry < m and graph[rx][ry]:
                
