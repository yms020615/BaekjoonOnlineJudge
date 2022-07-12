import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
diameter = []

visited = [0 for _ in range(n + 1)]
def dfs(u, dist):
    visited[u] = 1
    diameter.append([u, dist])

    for v, d in graph[u]:
        if not visited[v]:
            dfs(v, dist + d)
    

for i in range(1, n + 1):
    l = list(map(int, input().split()))

    v = l[0]
    for j in range(1, len(l) - 1, 2):
        graph[v].append([l[j], l[j + 1]])

dfs(1, 0)
farthest = max(diameter, key = lambda x: x[1])

visited = [0 for _ in range(n + 1)]
diameter = []
dfs(farthest[0], 0)
farthest2 = max(diameter, key = lambda x: x[1])

print(max(farthest[1], farthest2[1]))
