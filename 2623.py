import sys
input = sys.stdin.readline

from collections import defaultdict, deque

def topology_sort(graph):
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)


n, m = map(int, input().split())
graph = defaultdict(list)
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    s = list(map(int, input().split()))
    for i in range(1, s[0]):
        graph[s[i]].append(s[i+1])
        indegree[s[i+1]] += 1

result = []
topology_sort(graph)
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)
