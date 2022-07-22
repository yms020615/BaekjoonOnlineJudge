import sys
input = sys.stdin.readline

from itertools import permutations
a, b = map(int, input().split())
c = [i for i in range(1, a+1)]
d = list(permutations(c, b))
for i in d:
    print(*i)
