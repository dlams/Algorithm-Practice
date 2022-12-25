from sys import stdin
from collections import deque

# input = stdin.readline

n = int(input())
tree = list(map(int, input().split()))
removed_node = int(input())

def dfs(v):
    tree[v] = -2
    for i in range(n):
        if tree[i] == v:
            dfs(i)

dfs(removed_node)
res = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:
        res += 1
print(res)