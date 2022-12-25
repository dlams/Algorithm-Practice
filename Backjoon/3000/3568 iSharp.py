ty, *var = map(lambda x: x.rstrip(",;"), input().split())
# print(ty)
# print(*var)

for v in var:
    for idx in range(len(v)):
        # print(idx)
        a, b = v, ""
        if v[idx] in ["[", "]", "*", "&"]:
            a, b = v[:idx], v[idx:]
            break

    # b = b[::-1]
    print(ty, end="")
    for c in b[::-1]:
        if c == "[":
            print("]", end="")
        elif c == "]":
            print("[", end="")
        else:
            print(c, end="")
    print(" ", end="")
    print(a + ";")
