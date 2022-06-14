import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
arr = [(l[i], i+1) for i in range(n)]

def kth(start, end, k):
    count = 0
    for i in range(n):
        if start <= arr[i][1] <= end:
            count += 1
        if count == k:
            return arr[i][0]
    return -1

arr.sort()
for _ in range(m):
    i, j, k = map(int, input().split())
    print(kth(i, j, k))
