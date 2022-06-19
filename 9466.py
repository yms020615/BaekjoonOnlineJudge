import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v):
    global result
    visited[v] = 1
    traced.append(v)

    w = graph[v]
    if visited[w]:
        if w in traced:
            result += traced[traced.index(w):]
        return
    else:
        dfs(w)

for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            traced = []
            dfs(i)

    print(n - len(result))
