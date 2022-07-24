import sys
input = sys.stdin.readline

from itertools import permutations
n, m = map(int, input().split())
a = list(map(int, input().split()))
perm = []
for i in sorted(list(set(permutations(a, m)))):
    print(*i)
