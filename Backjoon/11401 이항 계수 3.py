# nCk = (n!) / (n-k)!k!
# 역원을 구해서 풀기
d = [0] * 4_000_001
d[:3] = [0, 1, 2]
n, k = map(int, input().split())

if (not k) or (not n - k):
    print(1)
    exit(0)


prime = int(1e9) + 7

# N! mod p 구하기
N = 1
for i in range(3, n + 1):
    d[i] = (d[i - 1] * i) % prime

N = d[n]
# Inverse Element = 역원
IE = pow(d[n - k] * d[k], -1, prime)

print((N * IE) % prime)
