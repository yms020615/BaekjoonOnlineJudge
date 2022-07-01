import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def re(x, n):
    return x - n if x > n else x + n

def dfs(node, visited, stack):
    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, visited, stack)
    stack.append(node)

def reverse_dfs(node, visited, stack):
    visited[node] = 1
    stack.append(node)
    for neighbor in reverse_graph[node]:
        if visited[neighbor] == 0:
            reverse_dfs(neighbor, visited, stack)

v, e = map(int, input().split())
graph = [[] for _ in range(2*v + 1)]
reverse_graph = [[] for _ in range(2*v + 1)]
for _ in range(e):
    i, j = map(int, input().split())
    if i < 0: i = -i + v
    if j < 0: j = -j + v
    graph[re(i, v)].append(j)
    graph[re(j, v)].append(i)
    reverse_graph[j].append(re(i, v))
    reverse_graph[i].append(re(j, v))

stack = []
visited = [0] * (2*v + 1)
for i in range(1, 2*v + 1):
    if visited[i] == 0:
        dfs(i, visited, stack)

visited = [0] * (2*v + 1)
sccList = []
while stack:
    vertexList = []
    node = stack.pop()
    if visited[node] == 0:
        reverse_dfs(node, visited, vertexList)
        sccList.append(sorted(vertexList))

for i in sccList:
    for j in i:
        if j > v:
            if j - v in i:
                print(0)
                exit(0)
        else:
            if j + v in i:
                print(0)
                exit(0)
print(1)
