import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
count = 0

visit = [0 for _ in range(n + 1)]
def dfs(u):
    global count
    visit[u] = 1

    for v in graph[u]:
        if not visit[v]:
            count += 1
            dfs(v)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(count)
