from collections import deque

while 1:
    try:
        a, b = input().split()
        a = deque(a)
        for c in b:
            if c == a[0]:
                a.popleft()
            if len(a) == 0:
                break
        print("Yes" if len(a) == 0 else "No")
    except:
        break