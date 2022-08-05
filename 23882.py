import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def selection_sort(a, k):
    for i in range(n-1, 0, -1):
        maxn = max(a[0:i+1])
        maxid = a.index(maxn)
        if i != maxid:
            a[i], a[maxid] = a[maxid], a[i]
            k -= 1
            if not k:
                return a
    return -1

ret = selection_sort(a, k)
if type(ret) == int:
    print(ret)
else:
    print(*ret)
