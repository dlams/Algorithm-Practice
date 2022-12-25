# BJ 11444
# 1_000_000_007로 나눈 나머지를 구해야함.
# 피사노 주기를 이용한 문제가 아닌 행렬 방식 사용
# 행렬로 표현하기
# ( Fn+2 )   ( 1 1 )( Fn+1 )
# ( Fn+1 ) = ( 1 0 )(  Fn  )
# 일반화하면,
# ( Fn+1 Fn )   ( 1 1 )^n
# ( Fn Fn-1 ) = ( 1 0 )
# 어떤 수의 K제곱은 O(logK)

mod = int(1e9) + 7


def MatrixProduct(arr1: list[list[int]], arr2: list[list[int]]):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            answer[i][j] %= mod
    return answer


def fibo(n: int):
    if n < 1:
        return 0
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2 == 1:
            ans = MatrixProduct(ans, a)
        a = MatrixProduct(a, a)
        n //= 2
    return ans[0][1]


n = int(input())
print(fibo(n))
