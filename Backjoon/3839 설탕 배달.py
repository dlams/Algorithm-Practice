n = int(input())

CONST = 5001
array = [3, 5]
d = [CONST] * (n + 1)

d[0] = 0
for dummy in array:
    for j in range(dummy, n + 1):
        if d[j - dummy] != CONST:
            d[j] = min(d[j], d[j - dummy] + 1)


if d[n] == CONST:
    print(-1)
else:
    print(d[n])