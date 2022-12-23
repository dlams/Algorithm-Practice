from math import gcd

n, a = map(int, input().split())

print(n - a, end=" ")
if gcd(a, n) != 1:
    print(-1)
else:
    print(pow(a, -1, n))
