input = __import__('sys').stdin.readline

import heapq

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()

heap = []
heapq.heappush(heap, l[0][1])

for i in range(1, n):
    if heap[0] > l[i][0]:
        heapq.heappush(heap, l[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, l[i][1])

print(len(heap))
