import sys
input = sys.stdin.readline

from math import sqrt

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [i for i in range(n+1)]
edge = []
ans = 0
point = [list(map(float, input().split())) for _ in range(n)]
for i in range(n-1):
    for j in range(i, n):
        edge.append((sqrt((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2), i, j))
edge.sort()

for i in edge:
    cost, x, y = i

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        ans += cost

print(ans)
