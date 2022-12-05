n, k = map(int, input().split())
array01 = list(map(int, input().split()))
array02 = list(map(int, input().split()))

array01.sort()
array02.sort(reverse=True)

for i in range(k):
    if array02[i] > array01[i]:
        array01[i], array02[i] = array02[i], array01[i]
    else:
        break

print(sum(array01))
