import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x, h, visited):
    visited[y][x] = 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] > h:
            dfs(ny, nx, h, visited)

ans = 0
for h in range(max(map(max, graph))):
    count = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i, j, h, visited)
                count += 1

    ans = max(ans, count)

print(ans)
