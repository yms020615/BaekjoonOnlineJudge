import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
m = max(dp)
l = []
for i in range(n-1, -1, -1):
    if dp[i] == m:
        l.append(a[i])
        m -= 1
print(*reversed(l))
