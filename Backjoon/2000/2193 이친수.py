n = int(input())

d = [0] * 90
d[:3] = [1, 1, 2]

for i in range(3, 90):
    d[i] = d[i - 1] + d[i - 2]
print(d[n - 1])