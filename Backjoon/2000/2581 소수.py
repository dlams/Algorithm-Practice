m = int(input())
n = int(input())

d = [True] * (n + 1)
prime = []
for i in range(2, n + 1):
    if d[i]:
        if m <= i <= n:
            prime.append(i)
        for idx in range(i, n + 1, i):
            d[idx] = False

if len(prime) > 0:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)