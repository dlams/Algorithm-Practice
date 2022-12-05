from sys import stdin

size = int(stdin.readline())
for _ in range(size):
    a, b = map(int, stdin.readline().strip().split())
    tmp = pow(a, b) % 10
    if not tmp:
        print(tmp)
    else:
        print(10)