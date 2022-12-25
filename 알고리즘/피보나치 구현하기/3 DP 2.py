# DP를 사용한 하향식 접근
# 시간 복잡도 : O(N)

n = 10
d = [0] * (n + 1)
d[:3] = [0, 1, 1]
for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])
