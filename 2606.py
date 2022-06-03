import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
c = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    c[x][y] = 1
    c[y][x] = 1

count = 0
def dfs(v):
    global count
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and c[v][i] == 1:
            count += 1
            dfs(i)

dfs(1)
print(count)
