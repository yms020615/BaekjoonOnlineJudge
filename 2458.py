import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if j not in graph[i]:
            graph[i][j] = float('inf')

def fw(graph):
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = graph[i][j]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

path = fw(graph)
ans = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if path[i][j] != float('inf') or path[j][i] != float('inf'):
            cnt += 1
    if cnt == n-1:
        ans += 1
print(ans)
