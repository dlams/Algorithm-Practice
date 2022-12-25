n = int(input())

a, b = 0, 1
for i in range(n + 1):
    b, a = a, a + b
print(b)
