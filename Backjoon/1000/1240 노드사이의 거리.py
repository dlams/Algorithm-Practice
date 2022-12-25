from sys import stdin
from collections import deque
Not Solved
# input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    to, fr, val = map(int, input().split())
    graph[to].append((fr, val))
    graph[fr].append(((to, val)))


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# def bfs(start, target):
#     visited = [False for _ in range(n+1)]
#     queue = deque([start])
#     # visited[start] = True
#     print(visited)
#     while queue:
#         v = queue.popleft()
#         if not visited[v]:
#             visited[v] = True
#             for node, value in graph[v]:
#                 print(node, value)
#                 queue.append(node)

print(graph)
for _ in range(m):
    s, t = map(int, input().split())
    print(s, t, "========")
    bfs(s, t)