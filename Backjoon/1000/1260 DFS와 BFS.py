from collections import deque

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()

def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not visted[node]:
            dfs(graph, node, visted)

def bfs(graph, v, visted):
    queue = deque([v])
    visted[v] = True
    print(v, end=' ')
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visted[i]:
                visted[i] = True
                queue.append(i)
                print(i, end=' ')


visted = [False] * (n + 1)
dfs(graph, start, visted)
print()
visted = [False] * (n + 1)
bfs(graph, start, visted)
