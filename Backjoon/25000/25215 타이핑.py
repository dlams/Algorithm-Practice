string = input()
res = len(string)
tmp = False

for i in range(len(string)):
    c = string[i]
    isUpper = c.isupper()

    if isUpper and not tmp:
        tmp = True
        res += 1
        if (i < len(string) - 1) and (string[i + 1].islower()):
            tmp = False
    elif tmp and not isUpper:
        tmp = False
        res += 1
        if (i < len(string) - 1) and (string[i + 1].isupper()):
            tmp = True
print(res)