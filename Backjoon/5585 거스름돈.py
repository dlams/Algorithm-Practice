# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
n = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

res = 0
for coin in coins:
    while n >= coin:
        n -= coin
        res += 1

print(res)