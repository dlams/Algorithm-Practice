# 이진 탐색 소스코드 구현 ( 재귀함수 )
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search_recursive(array, target, mid + 1, end)

# 이진 탐색 소스코드 구현 ( 반복문 )
def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 재귀함수를 통한 이진 탐색
print("recu :", binary_search_recursive(array, 3, 0, len(array) - 1))
# 반복문을 통한 이진 탐색
print("iter :", binary_search_iter(array, 3, 0, len(array) - 1))