from sys import stdin

n = int(stdin.readline())

array = set()

for _ in range(n):
    key = stdin.readline().strip().split()

    if len(key) == 1:
        if key[0] == "all":
            array = set([i for i in range(1, 21)])
        else:
            array = set()

    else:
        k, v = key[0], key[1]
        v = int(v)

        if k == "add":
            array.add(v)
        elif k == "remove":
            array.discard(v)
        elif k == "check":
            print( 1 if v in array else 0)
        elif k == "toggle":
            if v in array:
                array.discard(v)
            else:
                array.add(v)