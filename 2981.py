import sys
input = sys.stdin.readline

import math
n = int(input())
a = []
s = []
gcd = 0
for i in range(n):
    a.append(int(input()))
    if i == 1:
        gcd = abs(a[1] - a[0])
    gcd = math.gcd(abs(a[i] - a[i - 1]), gcd)
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        s.append(i)
        s.append(gcd // i)
s.append(gcd)
s = list(set(s))
s.sort()
for i in s:
    print(i, end=' ')
