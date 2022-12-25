n = int(input())

d = [0] * 51
def fibo(n):
    if n < 2:
        return 1
    if d[n]:
        return d[n]

    d[n] = (fibo(n - 2) + fibo(n - 1) + 1) % 1000000007
    return d[n]


print(fibo(n))