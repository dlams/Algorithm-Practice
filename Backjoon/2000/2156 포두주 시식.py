from sys import stdin
# input = stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
d = [0 for _ in range(n)]
if n <= 2:
    print(sum(array))
    exit(0)
#
d[0] = array[0]
# d[1] = array[1] + d[0]

for idx in range(0, n - 1):
    d[idx] = array[idx + 1] + d[idx]

print(d)