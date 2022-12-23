from itertools import combinations

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
b = combinations(array, r=m)
for i in sorted(b):
    print(*i)