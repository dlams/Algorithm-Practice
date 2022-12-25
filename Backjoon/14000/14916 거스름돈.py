n = int(input())

CONST_VALUE = 100001
d = [100001] * (n+1)
d[0] = 0
coins = [2, 5]

for coin in coins:
    for j in range(coin, n+1):
        if d[j - coin] != CONST_VALUE:
            d[j] = min(d[j], d[j - coin] + 1)

if d[n] == CONST_VALUE:
    print(-1)
else:
    print(d[n])