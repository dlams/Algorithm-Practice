from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
wei, val = [], []

for _ in range(n):
    w, v = map(int, input().split())
    wei.append(w)
    val.append(v)

d = [[0 for i in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n+1): # 세로
    for w in range(1, k+ 1): # 가로
        if wei[i - 1] <= w:
            d[i][w] = max(val[i - 1] + d[i-1][w - wei[i-1]], d[i - 1][w])
        else:
            d[i][w] = d[i - 1][w]

print(d[n][k])


# print("wei")
# print(" ", end='')
# print(1, 2, 3, 4, 5, 6, 7, sep="  ")
# print(*d, sep='\n')
# print(len(d))
# print(len(d[0]))

