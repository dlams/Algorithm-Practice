mod = int(1e9)


def MatrixProduct(arr1, arr2):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            answer[i][j] %= mod
    return answer


o, p = map(int, input().split())
o, p = o + 1, p + 2

ans = [[1, 0], [0, 1]]
a = [[1, 1], [1, 0]]
while o > 0:
    if o % 2 == 1:
        ans = MatrixProduct(ans, a)
    a = MatrixProduct(a, a)
    o //= 2
q = ans[0][1]

ans = [[1, 0], [0, 1]]
a = [[1, 1], [1, 0]]
while p > 0:
    if p % 2 == 1:
        ans = MatrixProduct(ans, a)
    a = MatrixProduct(a, a)
    p //= 2

print((ans[0][1] - q) % mod)
