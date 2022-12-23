from itertools import product
# PI

n, m = map(int, input().split())
for i in product(range(1, n + 1), repeat=m):
    print(*i)