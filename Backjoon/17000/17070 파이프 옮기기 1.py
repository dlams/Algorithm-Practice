from sys import stdin

# 입력을 빠르게 받기위한 stdin.readline 사용
input = stdin.readline

# n 입력받기
n = int(input())

# map 입력받기
array = [[] for _ in range(n)]
for idx in range(n):
    array[idx] = list(map(int, input().split()))

# dp를 활용하기 위한 저장공간 마련
# 0차원 y좌표, 1차원 x좌표, 2차원 수평 이동 개수, 수직 이동 개수, 대각선 이동 개수
# ex) d[y][x][0] => (x, y)에서 수평으로 가는 파이프 수
d = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

# 0번쨰 인덱스 dp 테이블 초기화
for idx in range(1, n):
    # 1이면 벽으로 막혀 있기 때문에 더이상 파이프를 놓을 수 없음 -> 종료
    if array[0][idx] == 1:
        break
    d[0][idx][0] = 1

# 맵 전체 탐색
for y in range(1, n):
    for x in range(1, n):
        # 놓을 자리가 벽으로 막혀있는 경우 continue
        if array[y][x] == 1:
            continue

        # 수평으로 연결된 경우
        d[y][x][0] += d[y][x - 1][0] + d[y][x - 1][2]
        # 수직으로 연결된 경우
        d[y][x][1] += d[y - 1][x][1] + d[y - 1][x][2]
        # 대각선으로 연결된 경우, 고려사항 발생
        if array[y - 1][x] == 0 and array[y][x - 1] == 0:
            d[y][x][2] += sum(d[y - 1][x - 1])

print(sum(d[n - 1][n - 1]))
