import sys
input = sys.stdin.readline

def five(n):
    k = 0
    while n != 0:
        n //= 5
        k += n
    return k

def two(n):
    k = 0
    while n != 0:
        n //= 2
        k += n
    return k

x, y = map(int, input().split())

if y == 0: print(0)
else: print(min(two(x)-two(y)-two(x-y), five(x)-five(y)-five(x-y)))
