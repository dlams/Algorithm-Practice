from sys import stdin

# input = stdin.readline

n, m = map(int, input().split())
array = [[0] * (n + 1)]
for _ in range(n):
    array.append([0] + list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n):
        array[i][j + 1] += array[i][j]

for j in range(1, n + 1):
    for i in range(1, n):
        array[i + 1][j] += array[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(array[x2][y2] - array[x1 - 1][y2] - array[x2][y1 - 1] + array[x1 - 1][y1 - 1])