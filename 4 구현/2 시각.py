N = int(input())

cnt = 0
for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            if str(hour).count("3 그리디") + str(minute).count("3 그리디") + str(second).count("3 그리디") > 0:
                cnt += 1
print(cnt)