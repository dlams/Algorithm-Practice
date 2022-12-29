# p(x) = n / x를 성립해야하기에
# n은 x의 배수가 아니라면 불가능

def factorization(x):
    d = 2
    res = set()
    while d <= x:
        if x % d == 0:
            # print(d)
            res.add(d)
            x = x / d
        else:
            d = d + 1
    return list(res)

n = int(input())

res = -1
for x in range(1, n + 1):
    if n % x != 0:
        continue
    tmp = 0
    for fac in factorization(x):
        tmp += (fac - 1) / fac
    # print(x, factorization(x))
    # print(tmp, round(x * x * tmp))
    if n == round(x * x * tmp):
        res = x
        break

print(res)