# BFS
from collections import deque

SIZE_COMPUTER = int(input())
SIZE_LINK = int(input())

graph = [ [] for _ in range(SIZE_COMPUTER + 1) ]
for _ in range(SIZE_LINK):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visted = [False] * (SIZE_COMPUTER + 1)

def bfs(graph, visted):
    result = -1
    queue = deque([1])
    visted[1] = True
    while queue:
        v = queue.popleft()
        result += 1
        for i in graph[v]:
            if not visted[i]:
                visted[i] = True
                queue.append(i)
    return result

print(bfs(graph, visted))