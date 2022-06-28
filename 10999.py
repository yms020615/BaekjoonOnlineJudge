import sys
input = sys.stdin.readline

def segment_init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = segment_init(start, mid, node * 2) + segment_init(mid + 1, end, node * 2 + 1)
    return tree[node]

def segment_sum(start, end, node, left, right):
    update_lazy(start, end, node)

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return segment_sum(start, mid, node * 2, left, right) + segment_sum(mid + 1, end, node * 2 + 1, left, right)

def update_lazy(start, end, node):
    if lazy[node]:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def segment_update(start, end, node, left, right, diff):
    update_lazy(start, end, node)

    if right < start or left > end:
        return
    
    if start >= left and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, left, right, diff)
    segment_update(mid + 1, end, node * 2 + 1, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
tree = [0 for _ in range(4 * n)]
lazy = [0 for _ in range(4 * n)]
segment_init(0, n-1, 1)

for _ in range(m+k):
    func = list(map(int, input().split()))

    if func[0] == 1:
        segment_update(0, n-1, 1, func[1] - 1, func[2] - 1, func[3])
    else:
        print(segment_sum(0, n-1, 1, func[1] - 1, func[2] - 1))
