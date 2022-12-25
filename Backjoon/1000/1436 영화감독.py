n = int(input())

res = 0
i = 0
while 1:
    i += 1
    if str(i).count("666") >= 1:
        res += 1
        if n == res:
            print(i)
            break