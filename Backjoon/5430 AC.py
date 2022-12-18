from sys import stdin
from collections import deque


for _ in range(int(input())):
    cmd = stdin.readline().strip()
    n = int(stdin.readline())
    arr = stdin.readline().rstrip()[1:-1].split(",")

    if n == 0:
        queue = deque()
    else:
        queue = deque(map(int, arr))

    check = 0
    for c in cmd:
        if c == "R":
            check = 1 - check
        else:
            if (len(queue)) < 1:
                check = -1
                print("error")
                break
            if check:
                queue.pop()
            else:
                queue.popleft()

    if not check:
        print("[", end="")
        print(*queue, sep=",", end="")
        print("]")
    elif check != -1:
        print("[", end="")
        queue.reverse()
        print(*queue, sep=",", end="")
        print("]")