input = __import__('sys').stdin.readline

from heapq import *

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

heap = [[] for _ in range(n + 1)]

heappush(heap[0], [0, 1])
heappush(heap[1], 0)

while heap[0]:
    cur_dist, cur_dest = heappop(heap[0])

    for new_dest, new_dist in graph[cur_dest]:
        new_dist += cur_dist

        if len(heap[new_dest]) < k:
            heappush(heap[new_dest], -new_dist)
            heappush(heap[0], [new_dist, new_dest])
        else:
            if -heap[new_dest][0] > new_dist:
                heappop(heap[new_dest])
                heappush(heap[new_dest], -new_dist)
                heappush(heap[0], [new_dist, new_dest])

for i in range(1, n + 1):
    if len(heap[i]) < k:
        print(-1)
    else:
        print(-heap[i][0])
