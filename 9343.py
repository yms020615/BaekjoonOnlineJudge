import sys
input = sys.stdin.readline

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

l = []
for i in range(int(input())):
    l.append(int(input()))

max_n = sorted(l, reverse = True)[0]
fact = [1, 1] + [0] * (2*max_n-1)
for i in range(2, 2*max_n+1):
    fact[i] = (i * fact[i-1]) % p

for n in l:
    if n == 1:
        print(1)
        continue
    ans = (((fact[2*n-1] % p) * (power((fact[n-1] * fact[n]), p-2) % p)) % p - ((fact[2*n-1] % p) * (power((fact[n-2] * fact[n+1]), p-2) % p)) % p) % p
    print(ans)
