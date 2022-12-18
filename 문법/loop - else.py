N = 5

for i in range(N):
    for j in range(N):
        if i + j >= 8:
            print("break", i, j, i + j)
            break
    else:
        print("else", i, j, i + j)
