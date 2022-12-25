from itertools import permutations

n, m = map(int, input().split())
array = map(int, input().split())

b = permutations(array, m)
for i in sorted(b):
    print(*i)