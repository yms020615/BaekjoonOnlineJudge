import sys
input = sys.stdin.readline

from itertools import permutations
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
perm = list(permutations(a, m))
for i in perm:
    print(*i)
