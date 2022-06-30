import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
for _ in range(n-1):
    _, c = map(int, input().split())
    l.append(c)

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n-i):
        x = i+j
        if j == x:
            continue

        dp[j][x] = 5000000000
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + l[j] * l[k+1] * l[x+1])

print(dp[0][-1])
