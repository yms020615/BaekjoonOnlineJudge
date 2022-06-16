input = __import__('sys').stdin.readline

k = int(input())

mob = [0] * 1000001

def mobius():
    mob[1] = 1
    for i in range(1, 1000001):
        if mob[i]:
            for j in range(2 * i, 1000001, i):
                mob[j] -= mob[i]

def sqf(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        k += mob[i] * (n // i ** 2)
    return k

l, h = 0, 100000000001
mobius()
while l+1 < h:
    m = (l + h) // 2
    if m - sqf(m) < k:
        l = m
    else:
        h = m

print(h)
