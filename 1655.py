import sys
input = sys.stdin.readline

import heapq
max_heap, min_heap = [], []

n = int(input())
for i in range(n):
    s = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, [-s, s])
    else:
        heapq.heappush(min_heap, [s, s])
    if len(max_heap) and len(min_heap) and max_heap[0][1] > min_heap[0][1]:
        max_value = -heapq.heappop(max_heap)[0]
        min_value = heapq.heappop(min_heap)[0]
        heapq.heappush(max_heap, [-min_value, min_value])
        heapq.heappush(min_heap, [max_value, max_value])
    print(max_heap[0][1])
