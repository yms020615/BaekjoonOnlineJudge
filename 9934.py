import sys
input = sys.stdin.readline

k = int(input())
a = [0] + list(map(int, input().split()))
ans = [[] for _ in range(k)]

def solve(n, depth):
    ans[depth].append(a[n])

    if depth == k - 1:
        return

    solve(n - 2 ** (k - depth - 2), depth + 1)
    solve(n + 2 ** (k - depth - 2), depth + 1)

solve(2 ** (k - 1), 0)

for i in ans:
    print(*i)
