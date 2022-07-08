import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {}
for i in range(N):
    graph[i+1] = {}

for i in range(M):
    a, b, c = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

def bellman_ford(graph, start):
    dist, pred = {}, {}
    for node in graph:
        dist[node] = float('inf')
        pred[node] = None
    dist[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + graph[node][neighbor]:
                    dist[neighbor] = dist[node] + graph[node][neighbor]
                    pred[neighbor] = node

    for node in graph:
        for neighbor in graph[node]:
            if dist[neighbor] > dist[node] + graph[node][neighbor]:
                print(-1)
                exit(0)

    return dist

ans = sorted(bellman_ford(graph, 1).items())[1:]
for k, v in ans:
    if v == float('inf'):
        print(-1)
    else:
        print(v)
