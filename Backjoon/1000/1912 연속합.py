n = int(input())
array = list(map(int, input().split()))
d = [-1001] * n

d[0] = array[0]
for i in range(1, n):
    d[i] = max(d[i - 1] + array[i], array[i])
print(max(d))