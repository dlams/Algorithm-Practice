mod = int(1e9) + 7


def MatrixProduct(arr1: list, arr2: list):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            answer[i][j] %= mod
    return answer


def fibo(n: int):
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2 == 1:
            ans = MatrixProduct(ans, a)
        a = MatrixProduct(a, a)
        n //= 2
    return ans[0][1]

o = int(input())
n = (o - 1) // 2 + 1
print((fibo(n * 2)) % mod)
