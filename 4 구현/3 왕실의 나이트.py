tmp = input()
x = ord(tmp[0]) - 96 - 1
y = int(tmp[1]) - 1

move = [
    [2, 1], [-2, 1], [2, -1], [-2, -1],
    [1, 2], [1, -2], [-1, 2], [-1, -2]
]
cnt = 0
for m in move:
    if 0 <= x + m[0] <= 7 and 0 <= y + m[1] <= 7:
        cnt += 1
print(cnt)
