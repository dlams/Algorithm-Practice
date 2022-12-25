from collections import deque

n, m, k, x = map(int, input().split())
graph = [ [] for _ in range(n + 1) ]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
visited = [ 0 ] * (n + 1)


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                # print("부모", v, "자식", i)
                queue.append(i)
                visited[i] = visited[v] + 1

bfs(x)
res = False
for idx in range(1, n + 1):
    if visited[idx] - 1 == k:
        res = True
        print(idx)

if not res:
    print(-1)