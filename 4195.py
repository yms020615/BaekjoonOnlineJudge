import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def simpleunion(i, j):
    x = simplefind(i)
    y = simplefind(j)

    if x == y:
        return
    else:
        parent[y] = x
        count[x] += count[y]


def simplefind(i):
    if i == parent[i]:
        return i

    p = simplefind(parent[i])
    parent[i] = p
    return parent[i]

f = int(input())
for _ in range(f):
    n = int(input())
    parent = {}
    count = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        simpleunion(a, b)
        print(count[simplefind(a)])
