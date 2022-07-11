import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n + 1)]

visited = [0 for _ in range(n + 1)]
def dfs(u):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = u
            dfs(v)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

for i in visited[2:]:
    print(i)
