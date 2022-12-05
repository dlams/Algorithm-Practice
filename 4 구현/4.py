# HMM
N, M = map(int, input().split())
x, y, facing = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(N) ]


# facing : North 0 # East stack.py # South 2 # West 3 그리디
facing_value = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def turn():
    global facing
    facing -= 1
    if facing < 0:
        facing = 3

cnt = 1
visited = set()
turn_time = 0
while True:
    turn()
    dx, dy = x + facing_value[facing][0], y + facing_value[facing][1]
    if maps[dx][dy] == 0:
        if (dx, dy) not in visited:
            visited.update((dx, dy))
            turn_time = 0
            maps[dx][dy] = 1
            x, y = dx, dy
            cnt += 1
            continue
    else:
        turn_time += 1
    if turn_time == 4:
        if maps[dx][dy] == 0:
            x, y = dx, dy
        else:
            break
        turn_time = 0
print(cnt)

