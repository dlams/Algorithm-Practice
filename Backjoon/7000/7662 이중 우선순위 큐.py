from heapq import heappush, heappop
NOT SOLVED

t = int(input())

for _ in range(t):
    q = []
    k = int(input())
    for i in range(k):
        query, value = input().split()
        value = int(value)
        if query == "I":
            heappush(q, value)
        else:
            if len(q) == 0:
                print("EMPTY")
            elif value == -1:
                print(heappop(q))