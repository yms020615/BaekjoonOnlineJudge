input = __import__('sys').stdin.readline

from decimal import *
getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP
pi = Decimal('3.14159265358979323846264338327950288419716939937510')

a, b, c = map(Decimal, input().split())

def sin(x):
    x %= 2 * pi
    n, prevX, currX, fact, powerX, sign = 0, 0, x, 1, x, 1
    x = x % (2 * pi)
    while prevX != currX:
        prevX = currX
        n += 1
        fact *= (2 * n + 1) * (2 * n)
        powerX *= x * x
        sign *= -1
        currX += powerX / fact * sign
    return +currX

left, right = Decimal('0'), Decimal('1000000')
while right - left > Decimal(1e-25):
    mid = (left + right) / 2
    if a * mid + b * Decimal(sin(mid)) < c:
        left = mid
    else:
        right = mid

print(round((left + right) / 2, 6))
