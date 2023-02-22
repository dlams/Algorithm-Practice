import sys
# from collections import deque

# input = sys.stdin.readline

n = int(input())
nodes = [[] for _ in range(n)]
visit = [False] * (n + 1)


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

def check():
    for idx in range(1, n):
        if not visit[idx]:
            return False
    return True
def dfs(n):
    for idx in 