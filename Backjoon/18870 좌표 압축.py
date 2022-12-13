from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split()))

nums2 = sorted(list(set(nums)))
# print(nums, nums2)
res = {nums2[i] : i for i in range(len(nums2))}

for i in nums:
    print(res[i], end = " ")