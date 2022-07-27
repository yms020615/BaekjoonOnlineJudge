import sys
input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))
dp = [[0] * 4 for i in range(max(a)+1)]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, max(a)+1):
    for j in range(1, 4):
        dp[i][j] = (dp[i-j][1] + dp[i-j][2] + dp[i-j][3] - dp[i-j][j]) % 1000000009

for i in a:
    print(sum(dp[i]) % 1000000009)
