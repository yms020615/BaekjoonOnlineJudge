import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [[0, 0]]
for _ in range(n):
    l.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = max(l[i][1] + dp[i-1][j-l[i][0]], dp[i-1][j]) if l[i][0] <= j else dp[i-1][j]
print(dp[n][k])
