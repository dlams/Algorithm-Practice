n = int(input())
array = list(map(int, input().split()))

dp = [0] * 100

dp[0] = array[0]
dp[1] = max(array[0], array[1])
for i in range(2, n):
    # ㅁㅁㅁㅁㅁㅁㅁㅁ <-i-1 ㅁ
    # i - 1번째 까지의 최대값과 i - 2까지의 최대값 + i를 비교 
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[n - 1])
print(dp[:n])