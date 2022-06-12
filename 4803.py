import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(w, v):
    visit[v] = 1
    for i in mat[v]:
        if i == w:
            continue
        if visit[i]:
            return False
        if not dfs(v, i):
            return False
    return True

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit(0)

    mat = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a].append(b)
        mat[b].append(a)

    count = 0
    for i in range(1, n+1):
        if not visit[i]:
            if dfs(0, i):
                count += 1

    if count == 0:
        print("Case %d: No trees." % case)
    elif count == 1:
        print("Case %d: There is one tree." % case)
    else:
        print("Case %d: A forest of %d trees." % (case, count))

    case += 1
