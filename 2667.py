import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)
n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
house = 0

def dfs(x, y):
    global house
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and apart[nx][ny] == '1':
            apart[nx][ny] = '0'
            house += 1
            dfs(nx, ny)
    return house

apart = [list(map(str, input().strip('\n'))) for _ in range(n)]

s = []
count = 0
for i in range(n):
    for j in range(n):
        if apart[i][j] == '1':
            s.append(dfs(i, j))
            count += 1
            house = 0
print(count)
for i in sorted(s):
    if i == 0:
        print(1)
    else:
        print(i)
