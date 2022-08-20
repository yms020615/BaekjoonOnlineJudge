input = __import__('sys').stdin.readline

from heapq import *

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int, input().split()))
    for i in a[1:]:
        heappush(heap, -i)

    if a[0] == 0:
        print(-heappop(heap) if heap else -1)
