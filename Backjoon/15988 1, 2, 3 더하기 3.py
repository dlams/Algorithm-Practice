n = int(input())

d = [0] * 1000001
d[1:6] = [1,1,3,3,4,8]

array = [int(input()) for _ in range(n)]

for i in range(7, max(array) + 1):
    d[i] = (d[i - 3] + d[i - 4] + d[i - 5] + 2 * d[i - 6]) % 1000000009

for i in range(n):
    print(d[array[i]])