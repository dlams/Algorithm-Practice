# DP를 사용한 재귀 개선
# 시간 복잡도 : O(N)

def fibonacci(n: int):
    if n <= 1:
        return n
    if not d[n]:
        d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]

n = 10
d = [0] * (n + 1)
print(fibonacci(n))
