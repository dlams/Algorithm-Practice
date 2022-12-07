from sys import stdin

for _ in range(int(stdin.readline())):
    h, w, n = map(int, stdin.readline().strip().split())

    num = n // h + 1
    floor = n % h
    if n % h == 0:
        num = n // h
        floor = h

    print(floor * 100 + num)
