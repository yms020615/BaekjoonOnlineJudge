input = __import__('sys').stdin.readline

def initMin(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(initMin(start, mid, node * 2), initMin(mid + 1, end, node * 2 + 1))
    return tree[node]

def queryMin(start, end, node, left, right):
    if start > right or end < left:
        return float('inf')

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(queryMin(start, mid, node * 2, left, right), queryMin(mid + 1, end, node * 2 + 1, left, right))

def segment_update(start, end, node, index, diff):
    if index < start or index > end:
        return
    
    if start == end:
        tree[node] = diff
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

n = int(input())
a = list(map(int, input().split()))
tree = [0 for _ in range(4*n)]
initMin(0, n-1, 1)

m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a[q[1]-1] = q[2]
        segment_update(0, n-1, 1, q[1]-1, q[2])
    else:
        print(a.index(queryMin(0, n-1, 1, 0, n-1)) + 1)
