n, k = map(int, input().split())
p = 1000000007

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n//2)
        return (y * y) % p
    else:
        y = power(x, (n-1)//2)
        return (x * y * y) % p

fact = [1, 1] + [0] * (n-1)
for i in range(2, n+1):
    fact[i] = (i * fact[i-1]) % p

ans = ((fact[n] % p) * (power((fact[k] * fact[n-k]), p-2) % p)) % p
print(ans)
