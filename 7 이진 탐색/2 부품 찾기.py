# 이진 탐색을 통해 구현하는 방법
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

SIZE_HAVE = int(input())
HAVE_INV = list(map(int, input().split()))
SIZE_NEED = int(input())
NEED_INV = list(map(int, input().split()))
HAVE_INV.sort()
for need in NEED_INV:
    if binary_search(HAVE_INV, need, 0, SIZE_HAVE - 1) == -1:
        print("no", end=" ")
    else:
        print("yes", end=" ")



# 계수 탐색을 통해 구현한 방법
SIZE_HAVE = int(input())
HAVE_INV = [0] * 1000001
for i in input().split():
    HAVE_INV[int(i)] = 1
SIZE_NEED = int(input())
NEED_INV = list(map(int, input().split()))

for need in NEED_INV:
    if HAVE_INV[need]:
        print("yes", end=" ")
    else:
        print("no", end=" ")



# N(가게의 부품 개수)을 입력받기
SIZE_HAVE = int(input())
HAVE_INV = set(map(int, input().split()))
SIZE_NEED = int(input())
NEED_INV = list(map(int, input().split()))

for i in NEED_INV:
    if i in HAVE_INV:
        print('yes', end=' ')
    else:
        print('no', end=' ')