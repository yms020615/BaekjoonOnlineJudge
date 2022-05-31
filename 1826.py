input = __import__('sys').stdin.readline

import heapq

n = int(input())
minHeap = []
for _ in range(n):
    heapq.heappush(minHeap, list(map(int, input().split())))
l, p = map(int, input().split())

maxHeap = []
count = 0
while p < l:
    while minHeap and minHeap[0][0] <= p:
        dist, fuel = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, [-fuel, dist])

    if not maxHeap:
        print(-1)
        exit(0)

    fuel, dist = heapq.heappop(maxHeap)
    p += -fuel
    count += 1

print(count)
