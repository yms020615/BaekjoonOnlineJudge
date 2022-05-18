import sys
input = sys.stdin.readline

from heapq import *

k, n = map(int, input().split())
l = list(map(int, input().split()))
heap = list(l)
heapify(heap)

for _ in range(n):
    head = heappop(heap)
    for j in range(k):
        heappush(heap, head * l[j])
        if head % l[j] == 0:
            break
print(head)
