n = int(input())

ans = '2', '0', '2', '3'

def check(req):
    cnt = 0
    for char in n:
        if ans[cnt] == char:
            cnt += 1
    return 1 if cnt == 4 else 0

res = 0
for i in range(2022, n):
    res += check(f'{i}')

print(res)