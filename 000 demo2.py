n, s = map(int, input().split())
board = [0]
board += list(map(int, input().split()))

d = [0] * (n + 1)
d2 = [0] * (n + 1)

r_maximum = 0
for i in range(s + 1, n + 1):
    d[i] = d[i - 1] + board[i]
    if d[i] < 0:
        break
    r_maximum = max(d[i], r_maximum)
for i in range(s - 1, 0, -1):
    d[i] = board[i] + r_maximum
    if d[i] < 0:
        break
    r_maximum += board[i]

l_maximum = 0
for i in range(s - 1, 0, -1):
    d2[i] = d2[i + 1] + board[i]
    if d2[i] < 0:
        break
    l_maximum = max(d2[i], l_maximum)

for i in range(s + 1, n + 1):
    d2[i] = board[i] + l_maximum
    if d2[i] < 0:
        break
    l_maximum += board[i]

# print(d)
# print(d2)
print(max(max(d), max(d2)))
