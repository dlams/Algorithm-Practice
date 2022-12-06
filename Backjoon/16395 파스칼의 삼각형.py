n, k = map(int, input().split())

d = [0] * 31
d[0] = 1
d[1] = 1
d[2] = 2


def factorial(x):
    if x <= 1:
        return 1
    if d[x] == 0:
        d[x] = x * factorial(x - 1)
    return d[x]



def combination(x, y):
    return factorial(x) // (factorial(x-y) * factorial(y))



print(combination(n - 1, k - 1))