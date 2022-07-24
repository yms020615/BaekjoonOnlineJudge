import sys
input = sys.stdin.readline

from itertools import combinations
a, b = map(int, input().split())
c = [i for i in range(1, a+1)]
d = list(combinations(c, b))
for i in d:
    print(*i)
