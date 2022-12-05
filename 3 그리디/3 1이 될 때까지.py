N, K = map(int, input().split())
cnt = 0

while 1:
    target = (N // K) * K
    cnt += (N - target)
    N = target
    if N < K:
        break
    cnt += 1
    N //= K

cnt += (N-1)
print(cnt)
