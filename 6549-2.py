import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 파이썬의 기본 재귀 깊이는 약 1000, 문제의 범위가 100000이기 때문에 늘리고 시작한다.

a = []
tree = []

def init(index, start, end): # 세그먼트 트리 초기화
    if start == end: # 세그먼트 트리의 리프 노드에
        tree[index] = start # 시작 인덱스를 넣어준다. 우리는 최솟값의 인덱스를 init과 query를 통해서 얻으려고 한다.
        return

    mid = (start + end) >> 1
    init(index << 1, start, mid) # 왼쪽 서브트리에 대해서 똑같은 과정
    init(index << 1 | 1, mid + 1, end) # 오른쪽 서브트리에 대해서 똑같은 과정

    if a[tree[index << 1]] <= a[tree[index << 1 | 1]]: # 배열의 값끼리 비교를 해서
        tree[index] = tree[index << 1] # 더 작은 값의 '인덱스'를 세그먼트 트리에 넣는다. (중요)
    else:
        tree[index] = tree[index << 1 | 1]

def query(index, start, end, left, right):
    if end < left or right < start: # 범위 체크
        return -1

    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) >> 1
    qLeft = query(index << 1, start, mid, left, right)
    qRight = query(index << 1 | 1, mid + 1, end, left, right)
    
    if qLeft == -1:
        return qRight
    elif qRight == -1:
        return qLeft
    else:
        if a[qLeft] <= a[qRight]: # 배열의 값끼리 비교를 해서
            return qLeft # 더 작은 값의 인덱스를 세그먼트 트리에 넣는 과정은 위와 같다.
        else:
            return qRight

def solve(left, right):
    m = query(1, 0, n - 1, left, right) # 최솟값의 인덱스를 가져온다.
    ret = (right - left + 1) * a[m] # 일단 현재 면적을 구한다.

    if left < m: # 왼쪽에 히스토그램이 남아 있으면
        ret = max(ret, solve(left, m - 1)) # 왼쪽으로 가서 탐색 후 현재 반환 값과 비교
    
    if m < right: # 오른쪽에 히스토그램이 남아 있으면
        ret = max(ret, solve(m + 1, right)) # 오른쪽으로 가서 탐색 후 현재 반환 값과 비교

    return ret

while True:
    h = list(map(int, input().split()))
    if len(h) == 1:
        break
    
    n = h[0]
    a = h[1:]
    tree = [0 for _ in range(4 * n)]
    init(1, 0, n - 1)

    print(solve(0, n - 1))
