from collections import deque
from collections import Counter


# DEQUE
queue = deque('hello world')
queue.append('!')
queue.popleft()
print(queue.pop())
### rotate(n) => queue.appendleft( queue.pop() ) * n ( n > 0 )
queue.rotate(1)
print(queue)
### rotate(n) => queue.append( queue.leftpop() ) * n ( n < 0 )
queue.rotate(-1)
print(queue)



# COUNTER
print(Counter("hello world"))
# 상위 n개 모두 출력
print(Counter("hello world").most_common())
# 상위 2개 출력
print(Counter("hello world").most_common(2))
