import sys
input = sys.stdin.readline

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

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
graph = []
cost = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

for i in range(e):
    c, a, b = graph[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c

print(cost)
