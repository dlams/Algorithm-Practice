n, k, prime = map(int, input().split())

# 특정 프라임 진법 구하기
def primeNatation(n, k):
    resN, resK = [], []
    while n:
        resN += [n % prime]
        resK += [k % prime]
        n //= prime
        k //= prime
    return resN, resK


d = [0] * 4_000_001
d[:3] = [0, 1, 2]

def combination(n, k):
    if k > n:
        return 0
    if (not k) or (not n - k):
        return 1
    for i in range(3, n + 1):
        if not d[i]:
            d[i] = (d[i - 1] * i) % prime

    N = d[n]
    # Inverse Element = 역원
    IE = pow(d[n - k] * d[k], -1, prime) % prime
    return N * IE

N, K = primeNatation(n, k)
res = 1
# print(N, K)
for i in range(len(N)):
    # print(combination(N[i], K[i]))
    res = (res * combination(N[i], K[i])) % prime

print(res)
