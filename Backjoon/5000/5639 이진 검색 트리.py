import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

lst = []
while 1:
    try:
        lst.append(int(input()))
    except:
        break


def post(s, e):
    if s > e:
        return
    m = e + 1
    for i in range(s + 1, e + 1):
        if lst[i] > lst[s]:
            m = i
            break
    post(s + 1, m - 1)
    post(m, e)
    print(lst[s])


post(0, len(lst) - 1)
