import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and cab[nx][ny] == 1:
            cab[nx][ny] = 0
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    cab = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        cab[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if cab[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
