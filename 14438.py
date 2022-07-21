import sys
input = sys.stdin.readline

def initMin(start, end, node):
    if start == end:
        tree_min[node] = a[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(initMin(start, mid, node * 2), initMin(mid + 1, end, node * 2 + 1))
    return tree_min[node]

def queryMin(start, end, node, left, right):
    if start > right or end < left:
        return float('inf')

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(queryMin(start, mid, node * 2, left, right), queryMin(mid + 1, end, node * 2 + 1, left, right))

def segment_update(start, end, node, index, diff):
    if index < start or index > end:
        return
    
    if start == end:
        tree_min[node] = diff
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)
    tree_min[node] = min(tree_min[node * 2], tree_min[node * 2 + 1])

n = int(input())
a = list(map(int, input().split()))
tree_min = [0 for _ in range(4 * n)]
initMin(0, n-1, 1)

m = int(input())
for _ in range(m):
    func = list(map(int, input().split()))

    if func[0] == 1:
        segment_update(0, n-1, 1, func[1] - 1, func[2])
    else:
        print(queryMin(0, n-1, 1, func[1] - 1, func[2] - 1))
