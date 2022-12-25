n = int(input())

a, b = 1, 1
for i in range(2, n + 1):
    a, b = (a + b) % 1000000007, a % 1000000007

print(b)