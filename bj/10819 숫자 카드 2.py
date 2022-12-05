from sys import stdin

size = int(stdin.readline())
nums = {}
for n in map(int, stdin.readline().strip().split()):
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1
stdin.readline()
for n in map(int, stdin.readline().strip().split()):
    if n in nums:
        print(nums[n], end=" ")
    else:
        print("0", end =" ")