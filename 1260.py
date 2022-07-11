import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visitD = [0 for _ in range(n + 1)]
def dfs(u):
    visitD[u] = 1

    for v in graph[u]:
        if not visitD[v]:
            print(v, end = ' ')
            dfs(v)

visitB = [0 for _ in range(n + 1)]
def bfs(u):
    visitB[u] = 1
    q = deque([])
    q.append(u)

    while q:
        curr = q.popleft()

        for v in graph[curr]:
            if not visitB[v]:
                visitB[v] = 1
                print(v, end = ' ')
                q.append(v)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

print(v, end = ' ')
dfs(v)
print()

print(v, end = ' ')
bfs(v)
