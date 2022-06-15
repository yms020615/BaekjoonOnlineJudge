from collections import deque

queue = deque([])
m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1
                queue.append([nx, ny])

k = 0
bfs()
for i in mat:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    k = max(k, max(i))
print(k - 1)
