# BFS
from collections import deque

SIZE_PEOPLE = int(input())
START, END = map(int, input().split())
SIZE_EDGE = int(input())

graph = [ [] for _ in range(SIZE_PEOPLE + 1) ]
for _ in range(SIZE_EDGE):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visted = [0] * (SIZE_PEOPLE + 1)

def bfs(graph, visted):
    queue = deque([START])
    visted[START] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visted[i]:
                visted[i] = visted[v] + 1
                queue.append(i)

bfs(graph, visted)
print(visted[END] - 1)