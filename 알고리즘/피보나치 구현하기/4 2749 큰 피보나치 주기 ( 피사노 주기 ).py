# M = 10^k 일때 k > 2 라면
# 피보나치의 주기는 항상 15 * 10^(k-1)

# 2749의 문제에서는 M이 10^6이기 떄문에 k = 6이지만 코드로 구할 수도 있음
n = int(input())
mod = 1_000_000
p = mod // 10 * 15
# k = 6
d = [0] * p # 5 = k - 1
d[:2] = [0, 1]
for i in range(2, len(d) - 1):
    d[i] = d[i - 1] + d[i - 2]
    d[i] %= mod
print(d[n % p])