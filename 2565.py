import sys
input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort()
l = [-1000000001]

for i in a:
    if l[-1] < i[1]:
        l.append(i[1])
    else:
        l[bisect_left(l, i[1])] = i[1]

print(n - len(l) + 1)
