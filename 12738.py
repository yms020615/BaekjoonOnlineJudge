import sys
input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
l = [-1000000001]

for i in a:
    if l[-1] < i:
        l.append(i)
    else:
        l[bisect_left(l, i)] = i

print(len(l)-1)
