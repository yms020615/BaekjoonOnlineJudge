import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
dp = [0] * (n+1)
dp[1] = a[1]
dp[2] = min(a[2], 2*a[1])
for i in range(3, n+1):
    dp[i] = a[i]
    for j in range(1, i//2+1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])
print(dp[n])
