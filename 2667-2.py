import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(n)] for _ in range(n)]
size = 0
def dfs(y, x):
    global size

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] == '1':
            visited[ny][nx] = 1
            size += 1
            dfs(ny, nx)

count = 0
ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            dfs(i, j)
            count += 1
            ans.append(size)
            size = 0

print(count)
for i in sorted(ans):
    print(i if i else 1)
