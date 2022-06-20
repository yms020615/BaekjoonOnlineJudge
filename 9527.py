import sys
input = sys.stdin.readline

from math import pow
a, b = map(int, input().split())

def solve(x):
    ret, prev, i, y = 0, 0, 1, x
    while x > i:
        if x & i:
            ret += prev + 1
            prev += x & i
            x -= i
        ret += x // 2
        i <<= 1

    return ret + (y - i + 1)

print(solve(b) - solve(a-1))
