import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = deque([])
    q.append([y, x])
    visited[y][x] = 1

    while q:
        curr = q.popleft()

        for i in range(4):
            ny = curr[0] + dy[i]
            nx = curr[1] + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = visited[curr[0]][curr[1]] + 1
                q.append([ny, nx])

bfs(0, 0)
print(visited[-1][-1])
