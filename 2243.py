input = __import__('sys').stdin.readline

def segment_init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = segment_init(start, mid, node * 2) + segment_init(mid + 1, end, node * 2 + 1)
    return tree[node]

def segment_update(start, end, node, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)

def query(start, end, node, k):
    if start == end:
        return start

    mid = (start + end) // 2
    if k <= tree[node * 2]:
        return query(start, mid, node * 2, k)
    else:
        return query(mid + 1, end, node * 2 + 1, k - tree[node * 2])

n = int(input())
a = [0] * 1000001
tree = [0] * (4000004)

for _ in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
        idx = query(1, 1000000, 1, q[1])
        print(idx)
        segment_update(1, 1000000, 1, idx, -1)
    else:
        segment_update(1, 1000000, 1, q[1], q[2])
