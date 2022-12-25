# nCk = (n!) / (n-k)!k!
# 역원을 구해서 풀기
d = [0] * 4_000_001
d[:3] = [0, 1, 2]
ei = [0] * 4_000_001
ei[:2] = [0, 1]
m = int(input())

NOT SOLVED

prime = int(1e9) + 7

for i in range(2, 4_000_001):
    if not d[i]:
        d[i] = (d[i - 1] * i) % prime
    # if not ei[i]:
    #     ei[i] = (ei[i - 1] * pow(i, -1, prime)) % prime

# for _ in range(m):
#     n, k = map(int, input().split())
#     if (not k) or (not n - k):
#         print(1)
#         continue
#     # N! mod p 구하기
#     N = d[n]
#     # Inverse Element = 역원
#     IE = ei[n - k + 1]
#
#     print((N * IE) % prime)
