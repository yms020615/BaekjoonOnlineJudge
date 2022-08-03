import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 3 for _ in range(1516)]
dp[1][1] = 1
for i in range(2, 1516):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000007
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 1000000007
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 1000000007
print(dp[n][0] % 1000000007)
