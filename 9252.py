import sys
input = sys.stdin.readline

a = [' '] + list(map(str, input().strip('\n')))
b = [' '] + list(map(str, input().strip('\n')))
dp = [['' for _ in range(len(b))] for _ in range(len(a))]

temp = 0
lcs = ''
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])
