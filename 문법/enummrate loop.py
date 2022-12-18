_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range를 쓰는 귀찮은 방법
for i in range(len(_list)):
    print(i, _list[i])

# enumerate로 간단한 구현
for idx, val in enumerate(_list):
    print(idx, val)
