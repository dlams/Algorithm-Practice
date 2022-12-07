from sys import stdin

n, m = map(int, stdin.readline().strip().split())

pw = dict()
for i in range(n):
    key, value = stdin.readline().strip().split()
    pw[key] = value
for i in range(m):
    print(pw[stdin.readline().strip()])