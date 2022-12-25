from sys import stdin, maxsize

# input = stdin.readline().strip
profit = 0
min_price = maxsize

n = input()
array = map(int, input().split())

# 최소 최대 갱신
for price in array:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)