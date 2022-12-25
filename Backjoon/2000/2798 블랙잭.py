from sys import stdin

n, m = map(int, stdin.readline().strip().split())
array = [ int(i) for i in stdin.readline().strip().split() ]

a = 100000
res = []
for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if i != j and i != k and j != k:
                if m - (array[i] + array[j] + array[k]) < 0:
                    continue
                if m - (array[i] + array[j] + array[k]) < a:
                    a = m - (array[i] + array[j] + array[k])
                    res = [array[i], array[j], array[k]]
print(sum(res))