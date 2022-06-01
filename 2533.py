import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(v):
    visited[v] = 1
    dp[v][0] = 1

    for i in tree[v]:
        if not visited[i]:
            dfs(i)
            dp[v][0] += min(dp[i][0], dp[i][1])
            dp[v][1] += dp[i][0]

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [0] * (n+1)

dfs(1)
print(min(dp[1][0], dp[1][1]))
