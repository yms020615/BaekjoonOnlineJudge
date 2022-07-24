import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement
a, b = map(int, input().split())
c = [i for i in range(1, a+1)]
for i in combinations_with_replacement(c, b):
    print(*i)
