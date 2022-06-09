import sys
input = sys.stdin.readline

from collections import deque

tc = int(input())

for _ in range(tc):
    n = int(input())
    indegree = [0] * (n+1)  
    graph = [[] for _ in range(n+1)]

    rank = list(map(int, input().split()))
    for i in range(0, n-1):
        for j in range(i+1, n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        check = True
        for i in graph[a]:
            if i == b:
                graph[a].remove(b)
                graph[b].append(a)
                indegree[b] -= 1
                indegree[a] += 1
                check = False
        if check:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
                    
                    
    impos = False
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    if not queue:
        impos = True

    while queue:
        if len(queue) > 1:
            impos = True
            break
        current = queue.popleft()
        result.append(current)

        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
            elif indegree[i] < 0:
                impos = True
                break

    if impos or len(result) < n:
        print('IMPOSSIBLE')
    else:
        print(*result)
