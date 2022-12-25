n, k = map(int, input().split())
array = [ i + 1 for i in range(n) ]

res = []
idx = 0
while array:
    idx = (idx + (k - 1)) % len(array)
    res.append(array.pop(idx))

print("<", end="")
print(*res, sep=", ", end="")
print(">", end="")
