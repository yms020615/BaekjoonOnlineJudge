import sys
input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
l = [-1000000001]

for i in range(n):
    if l[-1] < a[i]:
        l.append(a[i])
        dp[i] = len(l) - 1
    else:
        dp[i] = bisect_left(l, a[i])
        l[dp[i]] = a[i]

print(max(dp))
m = max(dp)
l = []
for i in range(n-1, -1, -1):
    if dp[i] == m:
        l.append(a[i])
        m -= 1
print(*reversed(l))
