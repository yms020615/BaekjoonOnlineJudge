import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
x = int(input())
a.sort()
l, r = 0, n-1
i = 0

while l < r:
    tmp = a[l] + a[r]
    if x == tmp: i += 1
    if x > tmp: l += 1; continue
    r -= 1
print(i)
