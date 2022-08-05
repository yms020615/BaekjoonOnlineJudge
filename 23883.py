import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

dic = {}
for i in range(len(a)):
    dic[a[i]] = i
m = sorted(a)

def selection_sort(a):
    global k

    for i in range(n-1, 0, -1):
        maxn = m.pop()
        maxid = dic[maxn]

        if i != maxid:
            a[i], a[maxid] = a[maxid], a[i]
            dic[a[maxid]] = dic[maxn]
            del dic[maxn]
            k -= 1

            if k == 0:
                print(a[maxid], a[i])
                exit(0)

selection_sort(a)
print(-1)
