n = int(input())

array = [False for _ in range(10 ** 6 + 1)]
res = 1
for i in range(2, n + 1):
    if array[i]:
        continue
    t = 1
    for j in range(i, n + 1, i):
        array[j] = True
        tmp = j
        cnt = 0
        while