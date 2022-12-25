n = int(input())
array = list(map(int, input().split()))

d = sorted(array)
res = []
for i in range(n):
    idx = d.index(array[i])
    print(idx, end=" ")
    d[idx] = -1
