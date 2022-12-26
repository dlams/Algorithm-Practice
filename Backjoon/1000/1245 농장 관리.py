from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]

# 상 하 좌 우 좌상 좌하 우상 우하
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(x, y, value):
    queue = deque([(x, y)])
    visited[y][x] = True
    res = 0
    check = False
    while queue:
        rx, ry = queue.popleft()
        for i in range(8):
            ox, oy = rx + dx[i], ry + dy[i]
            if 0 <= ox < m and 0 <= oy < n:
                if array[oy][ox] > value:
                    check = True
                if not visited[oy][ox] and array[oy][ox] == value:
                    res += 1
                    visited[oy][ox] = True
                    queue.append((ox, oy))
    return check
r = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            if not bfs(x, y, array[y][x]):
                r += 1
print(r)