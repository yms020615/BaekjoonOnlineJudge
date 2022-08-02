input = __import__('sys').stdin.readline

m = int(input())
f = [0] + list(map(int, input().split()))
dp = [[f[i]] for i in range(m+1)]
for j in range(1, 19):
    for i in range(1, m+1):
        dp[i].append(dp[dp[i][j-1]][j-1])

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())
    for i in range(18, -1, -1):
        if n >= 1 << i:
            n -= 1 << i
            x = dp[x][i]
    print(x)
