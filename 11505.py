import sys
input = sys.stdin.readline

mod = 1000000007

def segment_init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = (segment_init(start, mid, node * 2) * segment_init(mid + 1, end, node * 2 + 1)) % mod
    return tree[node]

def segment_multiply(start, end, node, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (segment_multiply(start, mid, node * 2, left, right) * segment_multiply(mid + 1, end, node * 2 + 1, left, right)) % mod

def segment_update(start, end, node, index, val):
    if index < start or index > end:
        return
    
    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, val)
    segment_update(mid + 1, end, node * 2 + 1, index, val)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % mod

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
tree = [0 for _ in range(4 * n)]
segment_init(0, n-1, 1)

for _ in range(m+k):
    func, x, y = map(int, input().split())

    if func == 1:
        a[x-1] = y
        segment_update(0, n-1, 1, x-1, y)
    else:
        print(segment_multiply(0, n-1, 1, x-1, y-1) % mod)
