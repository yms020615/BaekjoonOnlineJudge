import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, parent_v, dist):
    visited[v] = 1
    depth[v] = depth[parent_v] + 1

    if v != 1:
        dp[v] += dp[parent_v] + dist
    for next, value in graph[v]:
        if not visited[next]:
            parent[next][0] = v
            dfs(next, v, value)

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


def set_parent():
    dfs(1, 0, 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

n = int(input())
parent = [[0] * 21 for _ in range(n+1)]
depth = [0] * (n+1)
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

set_parent()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a] + dp[b] - 2 * dp[lca(a, b)])
