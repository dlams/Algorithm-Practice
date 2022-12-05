from sys import stdin
from collections import Counter

SIZE_NUM = int(stdin.readline())
numbers = []
for _ in range(SIZE_NUM):
    numbers.append(int(stdin.readline()))
numbers.sort()

print(round(sum(numbers)/SIZE_NUM))
print(numbers[SIZE_NUM // 2])

most = Counter(numbers).most_common()
if len(most) > 1:
    if most[0][1] == most[1][1]: print(most[1][0])
    else: print(most[0][0])
else: print(most[0][0])
print(numbers[-1] - numbers[0])