import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(graph):
    global indegree
    result = []
    heap = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        current = heapq.heappop(heap)
        result.append(current)

        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)

    return result

print(*topology_sort(graph))
