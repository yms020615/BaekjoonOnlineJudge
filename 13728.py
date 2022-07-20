input = __import__('sys').stdin.readline

from math import gcd

n = int(input())
if n == 1:
    print(1)
    exit(0)

fib = [0, 1] + [0] * 100010
for i in range(2, 100011):
    fib[i] = (fib[i-2] + fib[i-1]) % 1000000007
    
ans = 0
for i in range(1, n+1):
    ans += fib[gcd(i+1, n+1)]
    ans %= 1000000007
print(ans)
