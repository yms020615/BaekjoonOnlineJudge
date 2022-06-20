import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000000)
n = int(input())
a = [list(input().rstrip()) for _ in range(n)]
import copy
b = copy.deepcopy(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs1(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 'R':
            a[nx][ny] = 0
            dfs1(nx, ny)

def dfs2(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 'G':
            a[nx][ny] = 0
            dfs2(nx, ny)

def dfs3(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 'B':
            a[nx][ny] = 0
            dfs3(nx, ny)

count1 = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            dfs1(i, j)
            count1 += 1
        elif a[i][j] == 'G':
            dfs2(i, j)
            count1 += 1
        elif a[i][j] == 'B':
            dfs3(i, j)
            count1 += 1
        
a = copy.deepcopy(b)

for i in range(n):
    for j in range(n):
        if a[i][j] == 'G':
            a[i][j] = 'R'

count2 = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            dfs1(i, j)
            count2 += 1
        elif a[i][j] == 'B':
            dfs3(i, j)
            count2 += 1

print(count1, count2)
