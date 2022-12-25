a, b = map(int, input().split())

res = 0
while a != b:
    if a > b:
        res = -2
        break
    elif str(b)[-1] == "1":
        b //= 10
        res += 1
    elif b % 2 == 0:
        b //= 2
        res += 1
    else:
        res = -2
        break
print(res + 1)
