from sys import stdin

x = int(stdin.readline())
d = [0] * int(1e6 + 1)

for n in range(2, x + 1):
    d[n] = d[n - 1] + 1
    if not n % 2:
        d[n] = min(d[n], d[n // 2] + 1)
    if not n % 3:
        d[n] = min(d[n], d[n // 3] + 1)

print(d[x])