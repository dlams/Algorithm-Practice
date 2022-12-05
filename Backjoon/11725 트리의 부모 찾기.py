from collections import deque

SIZE_NODE = int(input())

graph = [ [] for _ in range(SIZE_NODE + 1) ]
for _ in range(SIZE_NODE - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False] * (SIZE_NODE + 1)


parent = {}

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # print("부모", v, "자식", i)
                parent[i] = v
                visited[i] = True


# def dfs(n):
#     visited[n] = True
#     for node in graph[n]:
#         if not visited[node]:
#             parent[node] = n
#             dfs(node)


# dfs(1)
bfs()
for node in range(2, SIZE_NODE + 1):
    print(parent[node])