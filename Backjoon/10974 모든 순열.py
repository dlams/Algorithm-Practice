from itertools import permutations

res = permutations([i for i in range(1, int(input()) + 1)])
for val in list(res):
    print(*val)
