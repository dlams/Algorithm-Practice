size = int(input())

array = []
for _ in range(size):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key=lambda x: x[1])
for name, _ in array:
    print(name, end=" ")