n = int(input())

def check(x):
    res = 0
    for c in str(x):
        res += int(c)
    return x + res

res = 0
for i in range(1, 1000001):
    if check(i) == n:
        res = i
        break

print(res)