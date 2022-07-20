import sys
input = sys.stdin.readline

from collections import deque

graph = []
visited = []

def bfs(u):
    q = deque([])
    q.append(u)
    ret = 1

    while q:
        curr = q.popleft()

        if visited[curr]:
            ret = 0

        visited[curr] = 1

        for v in graph[curr]:
            if not visited[v]:
                q.append(v)

    return ret

ans = []
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue 

        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n + 1)]
    res = 0

    for i in range(1, n + 1):
        if not visited[i]:
            res += bfs(i)

    ans.append(res)

for i in range(len(ans)):
    if ans[i] == 0:
        print('Case {}: No trees.'.format(i + 1))
    elif ans[i] == 1:
        print('Case {}: There is one tree.'.format(i + 1))
    else:
        print('Case {}: A forest of {} trees.'.format(i + 1, ans[i]))
