input = __import__('sys').stdin.readline

from math import gcd

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b:
        n, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - n * x1
        y0, y1 = y1, y0 - n * y1

    return x0, y0

for _ in range(int(input())):
    k, c = map(int, input().split())
    if k == c == 1:
        print(2)
        continue

    if gcd(k, c) != 1:
        print('IMPOSSIBLE')
    else:
        ans = extended_gcd(k, c)[1]
        while c * ans <= k:
            ans += k
        print('IMPOSSIBLE') if ans > 1e9 else print(ans)
