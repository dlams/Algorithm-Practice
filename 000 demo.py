k, d, a = map(int, input().split("/"))

if d == 0:
    print("hasu")
elif k + a < d:
    print("hasu")
else:
    print("gosu")