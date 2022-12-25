n, m = map(int, input().split())
named = set()
tmp = set()
for _ in range(n):
    named.add(input())
for _ in range(m):
    tmp.add(input())

print(len(named & tmp))
print(*(sorted(list(named & tmp))), sep="\n")
