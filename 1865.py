import sys
input = sys.stdin.readline

def bellman_ford(graph, start):
    dist = [0] * (N + 1)

    for i in range(N):
        for cur_node, next_node, cost in graph:
                if dist[cur_node] > dist[next_node] + cost:
                    dist[cur_node] = dist[next_node] + cost
                    if i == N - 1:
                        return 'YES'       
    return 'NO'

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    for i in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    for i in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))
    print(bellman_ford(graph, E))
