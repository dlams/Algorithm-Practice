n = int(input())
d = [0] * 101

d[1:6] = 1, 1, 1, 2, 2

for _ in range(n):
    k = int(input())
    for i in range(5, k+1):
        if d[i] == 0:
            d[i] = d[i - 1] + d[i - 5]
    print(d[k])