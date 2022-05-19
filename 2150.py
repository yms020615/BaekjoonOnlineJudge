import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
reverse_graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

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

stack = []
visited = [0] * (v+1)
for i in range(1, v+1):
    if visited[i] == 0:
        dfs(i, visited, stack)

visited = [0] * (v+1)
sccList = []
while stack:
    vertexList = []
    node = stack.pop()
    if visited[node] == 0:
        reverse_dfs(node, visited, vertexList)
        sccList.append(sorted(vertexList))

print(len(sccList))
for i in sorted(sccList):
    print(*i, -1)
