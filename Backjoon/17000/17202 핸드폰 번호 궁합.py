from sys import stdin

PHONE01 = [ int(i) for i in input() ]
PHONE02 = [ int(i) for i in input() ]

tmp01 = []
tmp02 = []

while len(PHONE01) != 1:
    for idx in range(len(PHONE01)):
        if idx <= len(PHONE02) - 1:
            tmp01.append((PHONE01[idx] + PHONE02[idx]) % 10)
        if idx < len(PHONE01) - 1:
            tmp02.append((PHONE01[idx + 1] + PHONE02[idx]) % 10)
            # print(tmp02)
    # break
    PHONE01 = tmp01.copy()
    PHONE02 = tmp02.copy()
    tmp01 = []
    tmp02 = []
    # print("="*10)
print(PHONE01[0], end="")
print(PHONE02[0])
