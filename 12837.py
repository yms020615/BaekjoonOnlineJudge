import sys
input = sys.stdin.readline

def segment_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return segment_sum(start, mid, node * 2, left, right) + segment_sum(mid + 1, end, node * 2 + 1, left, right)

def segment_update(start, end, node, index, val):
    if index < start or index > end:
        return
    
    if start == end:
        tree[node] += val
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, val)
    segment_update(mid + 1, end, node * 2 + 1, index, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

n, k = map(int, input().split())
a = [-1] + [0 for _ in range(n)]
tree = [0 for _ in range(4 * n)]

for _ in range(k):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        segment_update(1, n, 1, q[1], q[2])
    else:
        print(segment_sum(1, n, 1, q[1], q[2]))
