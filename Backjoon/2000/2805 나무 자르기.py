n, m = map(int, input().split())
trees = list(map(int, input().split()))


def get_cutting(m: int):
    res = 0
    for tree in trees:
        res += tree - m if tree - m > 0 else 0
    return res


start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2
    tmp = get_cutting(mid)
    if tmp >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)