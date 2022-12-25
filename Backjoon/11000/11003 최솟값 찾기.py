from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()
ans = []

for i in range(n):
    while queue and queue[-1][0] > arr[i]:
        queue.pop()
    while queue and queue[0][1] < i - l + 1:
        queue.popleft()
    queue.append((arr[i], i))
    print(queue[0][0], end=" ")