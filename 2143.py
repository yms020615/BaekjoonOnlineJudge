import sys
input = sys.stdin.readline

from itertools import accumulate
from collections import defaultdict 

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_sum = [[] for _ in range(n)]
b_sum = [[] for _ in range(m)]
for i in range(n):
    a_sum[i] = list(accumulate(a[i:]))
for i in range(m):
    b_sum[i] = list(accumulate(b[i:]))

A = defaultdict(int)
B = defaultdict(int)
for i in range(n):
    for j in range(len(a_sum[i])):
        A[a_sum[i][j]] += 1
for i in range(m):
    for j in range(len(b_sum[i])):
        B[b_sum[i][j]] += 1

ans = 0
for i in A.keys():
    if t-i in B:
        ans += B[t-i] * A[i]
print(ans)
