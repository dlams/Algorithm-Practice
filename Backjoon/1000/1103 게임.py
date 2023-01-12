from sys import stdin
input = stdin.readline

# BFS
from collections import deque

SIZE_COMPUTER, SIZE_LINK  = map(int, input().split())

graph = [ [] for _ in range(SIZE_COMPUTER + 1) ]
for _ in range(SIZE_LINK):
    v1, v2 = map(int, input().split())
    graph[v2].append(v1)
# print(graph)

def bfs(start):
    res = 0
    visited = [False] * (SIZE_COMPUTER + 1)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        res += 1
        for n in graph[node]:
            queue.append(n)
        #     print(n, "append")
        # print(node)
    return res

max_value = -1
res = []
for i in range(1, SIZE_COMPUTER + 1):
    # print("+++++++++++++++")
    tmp = bfs(i)
    if max_value < tmp:
        res = [i]
        max_value = tmp
    elif max_value == tmp:
        res.append(i)
    # print(tmp)
# print(res)
print(*res)