from sys import stdin
# input = stdin.readline

MAX_SIZE = 123_456 * 2 + 1

d = [True] * (MAX_SIZE)
prime = []

for i in range(2, MAX_SIZE):
    if d[i]:
        prime.append(i)
        for idx in range(i, MAX_SIZE, i):
            d[idx] = False

n = -1
n = int(input())
while n != 0:
    res = 0
    for idx, val in enumerate(prime):
        if n < val <= 2 * n:
            res += 1
        elif val > 2 * n:
            break
    print(res)

    # if n == 0:
    #     break
    n = int(input())
