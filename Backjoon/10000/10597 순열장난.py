n = input()

res = []
for i in n:
    if i == "0":
        res[len(res) - 1] = f"{res[len(res) - 1]}0"
    else:
        res.append(i)

print(' '.join(res))