import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

route = [[0] * (n+1) for _ in range(n+1)]

def path(i, j):
    if route[i][j] == 0:
        return []

    k = route[i][j]
    return path(i, k) + [k] + path(k, j)

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(c, dist[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                route[i][j] = k

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != float('inf') else 0, end = ' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] in [0, float('inf')]:
            print(0)
            continue
        ans = [i] + path(i, j) + [j]
        print(len(ans), end = ' ')
        print(*ans)
