n, m = map(int, input().split())
def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

if n % m == 0:
    print(0)
else:
    print(m - gcd(n, m))