import sys
input = sys.stdin.readline

k = int(input())

mob = [0] * 42000

def mobius():
    mob[1] = 1
    for i in range(42000):
        if mob[i]:
            for j in range(2 * i, 42000, i):
                mob[j] -= mob[i]

def sqf(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        k += mob[i] * (n // i ** 2)
    return k

l, h = 0, int(1.7 * k)
mobius()
while l+1 < h:
    m = (l + h) // 2
    if sqf(m) < k:
        l = m
    else:
        h = m

print(h)
