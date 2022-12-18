ALPHABET = 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1

def NAME2NUMS(name):
    return ALPHABET[ord(name) - 65]

NAME01 = [ NAME2NUMS(i) for i in input() ]
NAME02 = [ NAME2NUMS(i) for i in input() ]
tmp01 = []
tmp02 = []

while len(NAME01) != 1:
    for idx in range(len(NAME01)):
        if idx <= len(NAME02) - 1:
            tmp01.append((NAME01[idx] + NAME02[idx]) % 10)
        if idx < len(NAME01) - 1:
            tmp02.append((NAME01[idx + 1] + NAME02[idx]) % 10)
            # print(tmp02)
    # break
    NAME01 = tmp01.copy()
    NAME02 = tmp02.copy()
    tmp01 = []
    tmp02 = []
    # print("="*10)
print(NAME01[0], end="")
print(NAME02[0])