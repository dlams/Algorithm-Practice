from itertools import product

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
b = product(array, repeat=m)
for i in sorted(b):
    print(*i)