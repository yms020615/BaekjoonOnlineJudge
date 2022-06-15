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
        return 0
    
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return tree[node]

n = int(input())
a = [0] + list(map(int, input().split()))
b = dict(zip(list(map(int, input().split())), range(1, n+1)))
tree = [0] * (4*n)

ans = 0
for i in a[1:]:
    id = b[i]
    ans += segment_sum(1, n, 1, id, n)
    segment_update(1, n, 1, id, id)

print(ans)

