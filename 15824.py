import sys
input = sys.stdin.readline

def pow(x, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        y = pow(x, (n-1) // 2, mod) % mod
        return (x * y * y) % mod
    else:
        y = pow(x, n // 2, mod) % mod
        return (y * y) % mod

n = int(input())
sc = list(map(int, input().split()))
sc.sort()
ans = 0
for i in range(n):
    ans += ((pow(2, i, 1000000007) - pow(2, n-i-1, 1000000007)) * sc[i]) % 1000000007

print(int(ans % 1000000007))
