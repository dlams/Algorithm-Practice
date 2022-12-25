from sys import stdin
NOT SOLVED

input = stdin.readline


def pisanoPeriod(n: int):
    res = 0
    mod1, mod2 = 1, 2
    while not (mod1 == 1 and mod2 == 1):
        mod1, mod2 = mod2, (mod1 + mod2) % n
        res += 1
    return res + 1


q, m = map(int, input().split())
pp = pisanoPeriod(m)
d = [0] * (pp)
d[:3] = [1, 1, 2]

for i in range(2, pp):
    d[i] = (d[i - 1] + d[i - 2]) % m

for _ in range(q):
    a = int(input())
    print(d[a % pp - 1])
