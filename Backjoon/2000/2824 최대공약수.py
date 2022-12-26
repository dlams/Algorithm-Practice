from sys import stdin
input = stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

a, b = 1, 1
for i in range(n):
    a *= arr1[i]
for i in range(m):
    b *= arr2[i]

res = gcd(a, b)
print(str(res)[-9:])
