# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            # 현재의 위치 반환 ( 인덱스는 0부터 시작하기에 1 더함 )
            return i + 1
    return -1

array = [1, 5, 2, 3, 9, 8, 6, 7, 4]
print(sequential_search(len(array), 3, array))