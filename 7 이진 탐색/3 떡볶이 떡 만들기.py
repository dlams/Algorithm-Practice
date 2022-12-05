n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

def cutting(array, m):
    res = 0
    for i in array:
        if i >= m:
            res += i - m
    return res

def binary_search():
    global start, end
    while start <= end:
        mid = (start + end) // 2
        tmp = cutting(array, mid)
        if tmp == m:
            return mid
        elif tmp >= m:
            start = mid + 1
        else:
            end = mid - 1
    return None
print(binary_search())