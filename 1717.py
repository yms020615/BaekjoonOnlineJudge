import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def simpleunion(i, j):
    i = simplefind(i)
    j = simplefind(j)

    if i == j:
        return
    elif i > j:
        parent[i] = j
    else:
        parent[j] = i

def simplefind(i):
    if i == parent[i]:
        return i
    p = simplefind(parent[i])
    parent[i] = p
    return parent[i]

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        simpleunion(a, b)
    if k == 1:
        if simplefind(a) == simplefind(b):
            print('YES')
        else:
            print('NO')
