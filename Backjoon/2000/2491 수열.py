from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

d = [[1, 1] for _ in range(n)]
for i in range(1, n):
    if nums[i - 1] <= nums[i]:
        d[i][0] = d[i - 1][0] + 1
    if nums[i - 1] >= nums[i]:
        d[i][1] = d[i - 1][1] + 1

print(max(map(max, d)))