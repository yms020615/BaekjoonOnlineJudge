input = __import__('sys').stdin.readline

def dfs(v):
    if visited[v]:
        return 0
    visited[v] = 1
    for i in graph[v]:
        if slot[i] == 0 or dfs(slot[i]):
            slot[i] = v
            return 1
    return 0

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
slot = [0 for _ in range(m+1)]
for i in range(1, n+1):
    s = list(map(int, input().split()))
    for j in s[1:]:
        graph[i].append(j)

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
print(len(slot) - slot.count(0))
