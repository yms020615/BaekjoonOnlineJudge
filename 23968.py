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

        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                k -= 1
                dic[a[maxid]] = dic[maxn]

                if k == 0:
                    print(a[j], a[j+1])
                    exit(0)

        del dic[maxn]

selection_sort(a)
print(-1)
