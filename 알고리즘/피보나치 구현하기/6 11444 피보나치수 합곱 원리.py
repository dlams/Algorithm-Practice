# F(2n-1) = (Fn)^2 + (Fn-1)^2
# F2n = (Fn-1 + Fn+1)Fn = (2Fn-1 + Fn)Fn

# 메모리 너무 먹을 것 같은데?

mod = int(1e9) + 7

n = int(input())
d = [0] * 1_000_000_000_000_000_000


def fibo(n: int):
    if n < 1:
        return 0
    elif n <= 2:
        return 1
    elif not d[n]:
        return d[n]
    else:
        if n % 2 == 1:
            m = (n + 1) // 2
            t1 = fibo(m)
            t2 = fibo(m - 1)
            d[n] = t1 * t1 + t2 * t2
            d[n] %= mod
        else:
            m = n // 2
            t1 = fibo(m - 1)
            t2 = fibo(m)
            d[n] = (2 * t1 + t2) * t2
        return d[n]

n = int(input())
print(fibo(n))