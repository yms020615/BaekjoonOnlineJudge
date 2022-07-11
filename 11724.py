import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [0 for _ in range(n + 1)]
def dfs(u):
    visited[u] = 1

    for v in graph[u]:
        if not visited[v]:
            dfs(v)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
