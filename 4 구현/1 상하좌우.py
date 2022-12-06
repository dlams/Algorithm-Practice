N = int(input())
execute = input().split()
x, y = 1, 1

# L R U D
co = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for plan in execute:
    i = co.index(plan)
    if x + dx[i] < 1 or x + dx[i] > N or y + dy[i] < 1 or  y + dy[i] > N:
        continue
    x += dx[i]
    y += dy[i]
print(y, x)