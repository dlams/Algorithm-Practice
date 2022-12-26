from math import sqrt
NOT SOLVED

m, M = map(int, input().split())

d = [True] * (M + 1)
d[:2] = [False, True]


for i in range(2, int(sqrt(M)) + 1):   # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if d[i]:
        tmp = pow(i, 2)
        for j in range(pow(i, 2), M, pow(i, 2)):        # i의 배수 모두 False로 변환
            d[j] = False

# for i in range(2, int(sqrt(M)) + 1):
#   if d[i]:
#     tmp = pow(i, 2)
#     while tmp < M + 1:
#         d[tmp] = False
#         tmp *= i
print(d[:M+1])
print(sum(d[m:M+1]))