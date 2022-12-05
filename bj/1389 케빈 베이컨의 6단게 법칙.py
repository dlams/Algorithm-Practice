from collections import deque

SIZE_PEOPLE, SIZE_LINK = map(int, input().split())
graph = [ [] for _ in range(SIZE_PEOPLE + 1) ]
for i in range(SIZE_LINK):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
lenght = [ 0 ] * ( SIZE_PEOPLE + 1)



def bfs(start):
    queue = deque([start])
    lenght[start] = 1
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if lenght[node] == 0:
                lenght[node] = lenght[v] + 1
                queue.append(node)

res = []
for i in range(1, SIZE_PEOPLE + 1):
    bfs(i)
    res.append(sum(lenght[1:]) - lenght[i] - (SIZE_PEOPLE - 1))
    lenght = [ 0 ] * ( SIZE_PEOPLE + 1)
print(res.index(min(res)) + 1)