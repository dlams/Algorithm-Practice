def quickSort_original(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        quickSort_original(array, start, right - 1)
        quickSort_original(array, right + 1, end)




def quickSort_with_Python(array):
    if len(array) <= 0:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [i for i in tail if i < pivot]
    right = [i for i in tail if i >= pivot]

    return quickSort_with_Python(left) + [pivot] + quickSort_with_Python(right)


array = [9, 5, 2, 4, 1, 0, 7]

# 정통적인 방식의 퀵 정렬
quickSort_original(array, 0, len(array) - 1)
print(array)

array = [9, 5, 2, 4, 1, 0, 7]

# 파이썬의 특징을 잘 살린 퀵 정렬 변형
print(quickSort_with_Python(array))