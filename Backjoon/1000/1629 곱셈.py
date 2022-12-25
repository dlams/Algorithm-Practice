base, exp, mod = map(int, input().split())

res = 1
while exp:
    if exp % 2 == 1:
        res = (res * base) % mod
    base = (base * base) % mod
    exp //= 2

print(res)