import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

import random

n = int(input())

def pow(x, y, p):
    ret = 1
    x %= p
    while y > 0:
        if y % 2:
            ret = (ret * x) % p
        y //= 2
        x = (x * x) % p
    return ret

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        r = a % b
        a = b
        b = r
    return a

def factor(n):
    if prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2

    c = y = x = random.randrange(2, n)
    d = 1
    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x-y), n)
        if d == n:
            return factor(n)
    if prime(d):
        return d
    else:
        return factor(d)

def miller(n, a):
    k = n-1
    r = 0
    while k % 2 == 0:
        r += 1
        k //= 2

    x = pow(a, k, n)
    if x == 1 or x == n-1:
        return True
    for i in range(r-1):
        x = pow(x, 2, n)
        if x == n-1:
            return True
    return False

def prime(n):
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in l:
        if n == i:
            return True
        if not miller(n, i):
            return False
    return True

li = []
while n > 1:
    d = factor(n)
    li.append(d)
    n //= d

li.sort()

for i in li:
    print(i)
