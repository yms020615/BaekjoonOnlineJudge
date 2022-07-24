import sys
input = sys.stdin.readline

from itertools import product
a, b = map(int, input().split())
c = [i for i in range(1, a+1)]
if b == 1:
    for i in product(c):
        print(*i)
elif b == 2:
    for i in product(c, c):
        print(*i)
elif b == 3:
    for i in product(c, c, c):
        print(*i)
elif b == 4:
    for i in product(c, c, c, c):
        print(*i)
elif b == 5:
    for i in product(c, c, c, c, c):
        print(*i)
elif b == 6:
    for i in product(c, c, c, c, c, c):
        print(*i)
elif b == 7:
    for i in product(c, c, c, c, c, c, c):
        print(*i)
