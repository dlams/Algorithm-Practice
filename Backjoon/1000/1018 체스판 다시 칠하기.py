from sys import stdin
n, m = map(int, stdin.readline().strip().split())

array = [ stdin.readline().strip() for i in range(n) ]
# print(array)
r = []

for x in range(n - 7):
    for y in range(m - 7):
        res01 = 0
        res02 = 0
        for dx in range(x, x + 8):
            for dy in range(y, y + 8):
                if (dx + dy) % 2 == 0:
                    if array[dx][dy] == "B":
                        res01 += 1
                    else:
                        res02 += 1
                else:
                    if array[dx][dy] == "W":
                        res01 += 1
                    else:
                        res02 += 1


        r.append(min(res01, res02))

print(min(r))