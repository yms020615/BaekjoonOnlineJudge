import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
perm = list(combinations_with_replacement(a, m))
for i in perm:
    print(*i)
