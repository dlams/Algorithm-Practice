from collections import deque

n = int(input())
queue = deque([ i for i in range(1, n + 1)])

while queue:
    print(queue.popleft(), end=" ")
    if queue:
        queue.append(queue.popleft())
