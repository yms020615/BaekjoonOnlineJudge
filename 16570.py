import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
l = list(map(int, input().split()))

table = [0] * n
def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

l = list(reversed(l))
F = failure(l, table)
if not max(F):
    print(-1)
else:
    ans = dict(Counter(F))
    m = max(F)
    print(m, ans[m])
