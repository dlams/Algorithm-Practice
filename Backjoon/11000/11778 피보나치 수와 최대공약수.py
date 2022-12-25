def gcd(a: int, b: int):
    while b > 0:
        a, b = b, a % b
    return a


mod = int(1e9) + 7


def MatrixProduct(arr1, arr2):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            answer[i][j] %= mod
    return answer


n, m = map(int, input().split())
n = gcd(n, m)
if n < 1:
    print(0)
else:
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2 == 1:
            ans = MatrixProduct(ans, a)
        a = MatrixProduct(a, a)
        n //= 2
    print(ans[0][1])