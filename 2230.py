import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()

l, r = 0, 1
count = 0
ans = 2000000001
while l <= r and l < n and r < n:
    if a[r] - a[l] >= m:
        ans = min(ans, a[r] - a[l])
        l += 1
    else:
        r += 1

print(ans)
