input = __import__('sys').stdin.readline

from collections import deque
import heapq

n, l = map(int, input().split())
d = deque([])
a = list(map(int, input().split()))

for i in range(n):
    while d and d[-1][1] > a[i]:
        d.pop()
    while d and i - d[0][0] >= l:
        d.popleft()
    d.append((i, a[i]))
    print(d[0][1], end = ' ')
