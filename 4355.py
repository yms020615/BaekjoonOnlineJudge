import sys
input = sys.stdin.readline

isprime = [True] * 1000001
for i in range(2, int(1000001 ** 0.5) + 1):
    if isprime[i]:
        for j in range(2*i, 1000001, i):
            isprime[j] = False

pl = [i for i in range(2, 1000001) if isprime[i]]

def factor(n):
    fac = []
    for i in pl:
        if n % i == 0:
            fac.append(i)
    return fac

while True:
    n = int(input())
    if n == 0:
        break
    l = factor(n)
    for i in l:
        n *= (1 - 1 / i)
    print(int(n))
