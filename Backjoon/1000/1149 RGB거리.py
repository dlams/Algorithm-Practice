import sys

input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    d.append(list(map(int, input().split())))

for idx in range(1, n):
    d[idx][0] = min(d[idx - 1][1], d[idx - 1][2]) + d[idx][0]
    d[idx][1] = min(d[idx - 1][0], d[idx - 1][2]) + d[idx][1]
    d[idx][2] = min(d[idx - 1][0], d[idx - 1][1]) + d[idx][2]

print(min(d[idx]))