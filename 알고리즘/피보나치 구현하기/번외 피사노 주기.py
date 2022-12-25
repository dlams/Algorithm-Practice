def pisanoPeriod(n: int):
    res = 0
    mod1, mod2 = 1, 2
    while not (mod1 == 1 and mod2 == 1):
        mod1, mod2 = mod2, (mod1 + mod2) % n
        res += 1
    return res + 1