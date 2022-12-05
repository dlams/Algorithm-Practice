from collections import deque

queue = deque([ i for i in range(1, int(input()) + 1)])
cnt = 0
while len(queue) != 1:
    if cnt % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    cnt += 1
print(queue.popleft())