from sys import stdin

# input = stdin.readline
n, r = map(int, input().split())

d = [0] * (n + 1)
d[:3] = [1, 1, 2]
for i in range(3, n + 1):
    d[i] = d[i - 1] * i

print(d[n] // (d[r] * d[n - r]))