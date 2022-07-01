import sys
input = sys.stdin.readline

from heapq import *

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))
