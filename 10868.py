import sys
input = sys.stdin.readline

def initMin(start, end, node):
    if start == end:
        tree_min[node] = a[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(initMin(start, mid, node * 2), initMin(mid + 1, end, node * 2 + 1))
    return tree_min[node]

def initMax(start, end, node):
    if start == end:
        tree_max[node] = a[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(initMax(start, mid, node * 2), initMax(mid + 1, end, node * 2 + 1))
    return tree_max[node]

def queryMin(start, end, node, left, right):
    if start > right or end < left:
        return float('inf')

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(queryMin(start, mid, node * 2, left, right), queryMin(mid + 1, end, node * 2 + 1, left, right))

def queryMax(start, end, node, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(queryMax(start, mid, node * 2, left, right), queryMax(mid + 1, end, node * 2 + 1, left, right))

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
tree_min = [0 for _ in range(4 * n)]
tree_max = [0 for _ in range(4 * n)]
initMin(0, n-1, 1)
initMax(0, n-1, 1)

for _ in range(m):
    x, y = map(int, input().split())
    print(queryMin(0, n-1, 1, x-1, y-1))
