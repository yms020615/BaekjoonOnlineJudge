import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())

removeRoot, root = -1, -1
graph = [[] for _ in range(n + 1)]

for i in range(n):
    if a[i] == -1:
        root = i
        continue

    graph[a[i]].append(i)

    if i == m:
        removeRoot = a[i]

if m in graph[removeRoot]:
    graph[removeRoot].remove(m)

visited = [0 for _ in range(n + 1)]
count = 0
def dfs(u):
    global count

    visited[u] = 1
    if not graph[u]:
        count += 1
        return

    for v in graph[u]:
        if not visited[v]:
            dfs(v)

dfs(root)
print(count if a[m] != -1 else 0)
