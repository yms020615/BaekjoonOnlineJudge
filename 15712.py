import sys
input = sys.stdin.readline

a, r, n, mod = map(int, input().split())

def g(n):
    if n == 0:
        return 1
    if n == 1:
        return (r + 1) % mod
    if n % 2:
        return g(n // 2) * (1 + power(r, n // 2 + 1)) % mod
    return (g(n // 2 - 1) * (1 + power(r, n // 2)) % mod + power(r, n)) % mod

def power(x, n):
    ret = 1
    while n:
        if n % 2:
            ret *= x % mod
        x *= x % mod
        n //= 2
    return ret
        
ans = a * g(n-1) % mod
print(ans)
