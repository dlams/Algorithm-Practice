# 정의를 구현한 단수한 구현
# 시간 복잡도 : O(2^N)

def fibonacci(n: int):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(n))
