size = int(input())
serial = []
for _ in range(size):
    serial.append(input())

def sumInt(string):
    res = 0
    for c in string:
        if c.isdigit():
            res += int(c)
    return res

serial.sort(key=lambda x: (len(x), sumInt(x), x))

print(*serial, sep="\n")