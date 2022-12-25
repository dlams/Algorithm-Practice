r, c, w = map(int, input().split())

d = [0] * 31
d[0] = 1
d[1] = 1
d[2] = 2

def factorial(x):
    if x <= 1:
        return 1
    if d[x] == 0:
        d[x] = x * factorial(x - 1)
    return d[x]

def combination(x, y):
    return factorial(x) // (factorial(x-y) * factorial(y))

res = 0
for i in range(w):
    for j in range(c - 1, c + i):
        # print(r + i, "층", j, "번")
        # print(combination(r + i - 1, j))
        res += combination(r + i - 1, j)
print(res)
