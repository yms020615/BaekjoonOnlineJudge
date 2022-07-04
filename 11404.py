import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = c
    else:
        graph[a][b] = min(c, graph[a][b])
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

ans = fw(graph)
for i in range(n):
    for j in range(n):
        if i == j or ans[i+1][j+1] == float('inf'):
            print(0, end = ' ')
        else:
            print(ans[i+1][j+1], end = ' ')
    print()
