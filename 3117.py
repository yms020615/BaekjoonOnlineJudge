input = __import__('sys').stdin.readline

n, k, m = map(int, input().split())
movie = [0] + list(map(int, input().split()))
recommend = [0] + list(map(int, input().split()))
dp = [[recommend[i]] for i in range(k+1)]
for j in range(1, 31):
    for i in range(1, k+1):
        dp[i].append(dp[dp[i][j-1]][j-1])

for i in range(1, n+1):
    x, y = m-1, movie[i]
    for j in range(30, -1, -1):
        if x >= 1 << j:
            x -= 1 << j
            y = dp[y][j]
    print(y, end = ' ')
