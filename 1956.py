import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inf = 100000000
dist = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

temp = inf
for i in range(1, n+1):
    temp = min(temp, dist[i][i])

if temp == inf:
    print(-1)
else:
    print(temp)
