from math import pow, sqrt

x1, y1, x2, y2, x3, y3 = map(int, input().split())

def dr(a, b, c, d):
    return sqrt(pow(d - b, 2) + pow(c - a, 2))

if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
    print(-1)
else:
    p = dr(x1, y1, x2, y2)
    q = dr(x1, y1, x3, y3)
    r = dr(x2, y2, x3, y3)

    res = [2 * (p + q), 2 * (q + r), 2 * (p + r)]
    res.sort()

    print(res[2] - res[0])
