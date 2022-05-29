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
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return segment_sum(start, mid, node * 2, left, right) + segment_sum(mid + 1, end, node * 2 + 1, left, right)

def segment_update(start, end, node, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)

n, m = map(int, input().split())
a = [0 for _ in range(n+1)]
tree = [0 for _ in range(4 * n)]
segment_init(0, n-1, 1)

for _ in range(m):
    func, arg1, arg2 = map(int, input().split())
    if func == 0:
        if arg1 > arg2:
            arg1, arg2 = arg2, arg1
        print(segment_sum(0, n-1, 1, arg1 - 1, arg2 - 1))
    else:
        arg1 -= 1
        diff = arg2 - a[arg1]
        a[arg1] = arg2
        segment_update(0, n-1, 1, arg1, diff)
