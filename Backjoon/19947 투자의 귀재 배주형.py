# 초기 비용 H와 투자 기간 Y 입력
h, y = map(int, input().split())

d = [ h ] * (y + 1)

for i in range(1, y + 1):
    res = [int(d[i - 1] * 1.05)]
    if i >= 5:
        res.append(int(d[i - 5] * 1.35))
    if i >= 3:
        res.append(int(d[i - 3] * 1.2))

    d[i] = max(res)

print(d[y])