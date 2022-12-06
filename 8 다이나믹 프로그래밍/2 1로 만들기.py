# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programing) 진행 ( 보텀업 )
for n in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[n] = d[n - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if not n % 2:
        d[n] = min(d[n], d[n // 2] + 1)
    # 현재의 수가 3로 나누어 떨어지는 경우
    if not n % 3:
        d[n] = min(d[n], d[n // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if not n % 5:
        d[n] = min(d[n], d[n // 5] + 1)

print(d[x])