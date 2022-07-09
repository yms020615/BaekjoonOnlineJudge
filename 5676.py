import sys
input = sys.stdin.readline

a = []
tree = []

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def segment_init(start, end, node):
    if start == end:
        tree[node] = sign(a[start])
        return tree[node]

    mid = (start + end) // 2
    tree[node] = segment_init(start, mid, node * 2) * segment_init(mid + 1, end, node * 2 + 1)
    return sign(tree[node])

def segment_multiply(start, end, node, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return sign(tree[node])

    mid = (start + end) // 2
    return segment_multiply(start, mid, node * 2, left, right) * segment_multiply(mid + 1, end, node * 2 + 1, left, right)

def segment_update(start, end, node, index, val):
    if index < start or index > end:
        return
    
    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, val)
    segment_update(mid + 1, end, node * 2 + 1, index, val)
    tree[node] = tree[node * 2] * tree[node * 2 + 1]

while True:
    try:
        n, k = map(int, input().split())
        a = [-1] + list(map(int, input().split()))

        tree = [0 for _ in range(4 * n)]
        segment_init(1, n, 1)

        ans = ''
        for _ in range(k):
            q = input().rstrip().split()
            
            if q[0] == 'C':
                segment_update(1, n, 1, int(q[1]), sign(int(q[2])))
            else:
                temp = segment_multiply(1, n, 1, int(q[1]), int(q[2]))
                if temp > 0:
                    ans += '+'
                elif temp == 0:
                    ans += '0'
                else:
                    ans += '-'
        print(ans)

    except Exception:
        break
