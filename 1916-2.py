import sys
input = sys.stdin.readline

from heapq import *

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
heap = []
dist = [float('inf') for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())
visited = [0 for _ in range(n + 1)]

def dijkstra(start):
    dist[start] = 0
    heappush(heap, [0, start])

    while heap:
        curr_dist, curr_dest = heappop(heap)

        if dist[curr_dest] < curr_dist:
            continue

        for next_dest, next_dist in graph[curr_dest]:
            cost = curr_dist + next_dist

            if cost < dist[next_dest]:
                dist[next_dest] = cost
                heappush(heap, [cost, next_dest])

dijkstra(start)
print(dist[end])
