import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    min = 0
    for j in range(i):
        if a[i] > a[j]:
            min = max(min, dp[j])
    dp[i] = min + 1
print(max(dp))
