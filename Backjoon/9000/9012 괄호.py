from sys import stdin

n = int(input())
for _ in range(n):
    tmp = stdin.readline().strip()
    while tmp.count('()') != 0:
        tmp = tmp.replace('()', '')
    if len(tmp) == 0:
        print("YES")
    else:
        print("NO")