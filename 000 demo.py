big = []
small = []
for _ in range(3):
    a, b, c, d, pos, e, f, g, h = input().split()
    if pos == ">":
        big.append(set([a, b, c, d]))
        small.append(set([e, f, g, h]))
    elif pos == "<":
        small.append(set([a, b, c, d]))
        big.append(set([e, f, g, h]))
    else:
        print("indefinite")
        exit(0)

plus = big[0] & big[1] & big[2]
minus = small[0] & small[1] & small[2]
if len(plus) == 1:
    print(list(plus)[0], "+", sep="")
elif len(minus) == 1:
    print(list(minus)[0], "-", sep="")
else:
    print("impossible")

