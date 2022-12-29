from collections import defaultdict, deque

d = defaultdict(set)

for _ in range(int(input())):
    fr, to = input().split(" is ")
    d[fr].add(to)
    # d[to].add(fr)

def bfs(p, target):
    visited = []
    queue = deque([p])
    while queue:
        node = queue.popleft()
        if node not in visited:
            if node == target:
                return "T"
            visited.append(node)

            for n in d[node]:
                queue.append(n)
    return "F"

for _ in range(int(input())):
    fr, to = input().split(" is ")
    print(bfs(fr, to))