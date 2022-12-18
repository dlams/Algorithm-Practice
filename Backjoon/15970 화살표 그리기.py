from sys import stdin

array = [[], []]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().strip().split())
    array[b - 1].append(a)
array[0].sort()
array[1].sort()

dist = [[], []]
if len(array[0]) >= 2:
    dist[0].append(array[0][1] - array[0][0])
if len(array[1]) >= 2:
    dist[1].append(array[1][1] - array[1][0])

if len(array[0]) > 2:
    for i in range(1, len(array[0]) - 1):
        dist[0].append(min(array[0][i] - array[0][i - 1], array[0][i + 1] - array[0][i]))
if len(array[1]) > 2:
    for i in range(1, len(array[1]) - 1):
        dist[1].append(min(array[1][i] - array[1][i - 1], array[1][i + 1] - array[1][i]))

if len(array[0]) >= 2:
    dist[0].append(array[0][-1]- array[0][-2])
if len(array[1]) >= 2:
    dist[1].append(array[1][-1]- array[1][-2])
print(sum(dist[0] + dist[1]))
