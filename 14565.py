input = __import__('sys').stdin.readline

from math import gcd

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b:
        n, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - n * x1
        y0, y1 = y1, y0 - n * y1

    return x0, y0

n, a = map(int, input().split())
print(n - a, end = ' ')

if gcd(n, a) != 1:
    print(-1)
    exit(0)

ans = extended_gcd(n, a)[1]
while ans < 0:
    ans += n
print(ans)
