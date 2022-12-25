n = int(input())

d = [0] * 36
d[0] = 1
d[1] = 1
# d[2] = 2

for i in range(2, n + 1):
    tmp = 0
    for j in range(i + 1):
        tmp += d[j] * d[i - j - 1]
    d[i] = tmp

print(d[n])
