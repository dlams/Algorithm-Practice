# 정수 N과 M을 입력받음
n, m = map(int, input().split())
# N개의 화폐 단위를 입력받기
coins = []
for _ in range(n):
    a, b = map(int, input().split())
    coins.append([a, b])

# 한 번 계산된 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [ 10001 ] * (m + 1)

# 다이나믹 프로그래밍 진행(Dynamic Programing) 진행(보텀업)
dp[0] = 0
for i in range(n):
    for j in range(coins[i], m + 1):
        if dp[j - coins[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

# 계산된 결과 출력
if dp[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[m])

print(dp)