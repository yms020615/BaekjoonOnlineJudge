import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
for i in sorted(list(set(combinations_with_replacement(a, m)))):
    print(*i)
