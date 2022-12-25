from itertools import combinations_with_replacement

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
b = combinations_with_replacement(array, m)
for i in sorted(b):
    print(*i)