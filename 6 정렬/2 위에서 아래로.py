size = int(input())

nums = []
for _ in range(size):
    nums.append(int(input()))

nums.sort(reverse=True)
print(*nums)