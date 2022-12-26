from sys import stdin
input = stdin.readline

def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

def euler_phi(n: int):
    res = 1
    if n <= 0:
        return -1
    for idx in range(2, n):
        if gcd(idx, n) == 1:
            res += 1
    return res

while 1:
    n = int(input())
    if n == 0:
        break
    print(euler_phi(n))