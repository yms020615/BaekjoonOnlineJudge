import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if dist[i][j] != float('inf') or dist[j][i] != float('inf'):
            cnt += 1
    print(n - cnt - 1)
