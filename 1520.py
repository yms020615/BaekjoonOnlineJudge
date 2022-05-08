import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
v = [[-1] * n for _ in range(m)]

def dfs(x, y):
    global ans
    if x == m-1 and y == n-1:
        return 1
    if v[x][y] != -1:
        return v[x][y]
    v[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if l[nx][ny] < l[x][y]:
                v[x][y] += dfs(nx, ny)
    return v[x][y]

print(dfs(0, 0))
