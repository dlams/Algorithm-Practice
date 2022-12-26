from sys import stdin
input = stdin.readline

n = int(input())
array = [([0] * n) for _ in range(n)]
value = [([0] * n) for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    array[i][:len(a)] = a
value[0][0] = array[0][0]

for y in range(n - 1):
    for x in range(y + 1):
        value[y + 1][x] = max(value[y][x] + array[y + 1][x], value[y + 1][x])
        value[y + 1][x + 1] = max(value[y][x] + array[y + 1][x + 1], value[y + 1][x + 1])
print(max(value[n - 1]))
