import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

count = 0
for i in range(len(a)-1, -1, -1):
    if a[i] <= m:
        k = m // a[i]
        m -= k * a[i]
        count += k
print(count)
