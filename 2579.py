import sys
input = sys.stdin.readline

n = int(input())
s = []
dp = [0 for _ in range(n+2)]
for _ in range(n):
    s.append(int(input()))
s.append(0)
s.append(0)

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
print(dp[n-1])
