n = int(input())
prime = int(1e9) + 7
res = 0
for i in range(n):
    a, b = map(int, input().split())
    res += (a * b * pow(2, b-1, prime)) % prime
print(res % prime)
