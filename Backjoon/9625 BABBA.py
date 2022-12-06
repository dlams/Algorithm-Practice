n = int(input())

a = [0] * 47
b = [0] * 47

a[1] = 1
b[1] = 0

for i in range(2, n + 2):
    a[i] = b[i - 1]
    b[i] = a[i - 1] + b[i - 1]

print(a[n + 1], b[n + 1])