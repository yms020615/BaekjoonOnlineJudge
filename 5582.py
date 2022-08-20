input = __import__('sys').stdin.readline

a = input().rstrip()
b = input().rstrip()

len_a, len_b = len(a), len(b)

dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

ans = 0
for i in dp:
    ans = max(ans, max(i))

print(ans)
