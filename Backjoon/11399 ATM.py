size = int(input())

nums = [int(i) for i in input().split()]

nums.sort()

total_time = 0
for id in range(size):
    total_time += sum(nums[:id + 1])
print(total_time)