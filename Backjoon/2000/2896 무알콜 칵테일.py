juice = list(map(int, input().split()))
i, j, k = map(int, input().split())

total = i + j + k
rate = i/total, j/total, k/total

maximum = 0
for i in range(1, 3):
    # print(rate[i], juice[i] % rate[i])
    if juice[i] // rate[i] < juice[maximum] // rate[maximum]:
        maximum = i

res = juice[maximum] / rate[maximum]
for i in range(3):
    print(juice[i] - (rate[i] * res), end = " ")