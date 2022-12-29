from collections import deque

n, m, r = map(int, input().split())
array = [[] for _ in range(n + 1)]
for i in range(m):
    fr, to = map(int, input().split())
    array[fr].append(to)
    array[to].append(fr)
for i in range(n + 1):
    array[i].sort()

visited = [False] * (n + 1)

res = 0

queue = deque([r])

while queue:
    node = queue.popleft()

    if not visited[node]:
        print(node)
        res += 1
        visited[node] = True
        for nd in array[node]:
            queue.append(nd)

for _ in range(n - res):
    print(0)
