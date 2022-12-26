from collections import deque

n, m = map(int, input().split())
array = [list(i for i in input()) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    # print("=============")
    queue = deque([(x, y)])
    visited[y][x] = True
    sheep, wolf = 0, 0
    if array[y][x] == "v":
        wolf += 1
    elif array[y][x] == "o":
        sheep += 1
    while queue:
        rx, ry = queue.popleft()
        for i in range(4):
            ox, oy = rx + dx[i], ry + dy[i]
            if 0 <= ox < m and 0 <= oy < n:
                if array[oy][ox] == "#":
                    continue
                if not visited[oy][ox]:
                    # print(ox, oy, array[oy][ox])
                    if array[oy][ox] == "v":
                        wolf += 1
                    elif array[oy][ox] == "o":
                        sheep += 1
                    visited[oy][ox] = True
                    queue.append((ox, oy))
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return sheep, wolf

sheep, wolf = 0, 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and array[y][x] != "#":
            a, b = bfs(x, y)
            sheep += a
            wolf += b
print(sheep, wolf)