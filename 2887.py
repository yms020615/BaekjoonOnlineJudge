input = __import__('sys').stdin.readline

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

edge1 = []
edge2 = []
edge3 = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    edge1.append((x, i))
    edge2.append((y, i))
    edge3.append((z, i))
edge1.sort()
edge2.sort()
edge3.sort()

edge = []
for i in range(n-1):
    edge.append((abs(edge1[i+1][0] - edge1[i][0]), edge1[i][1], edge1[i+1][1]))
    edge.append((abs(edge2[i+1][0] - edge2[i][0]), edge2[i][1], edge2[i+1][1]))
    edge.append((abs(edge3[i+1][0] - edge3[i][0]), edge3[i][1], edge3[i+1][1]))
edge.sort()

result = 0
for i in edge:
    cost, x, y = i

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
print(result)
