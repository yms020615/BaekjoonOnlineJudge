n = int(input())
a = sorted(list(map(int, input().split())))

_ = int(input())
b = list(map(int, input().split()))

def bs(x, l, h):
    if l > h:
        return 0

    m = (l + h) // 2

    if x == a[m]:
        return 1
    elif x < a[m]:
        return bs(x, l, m-1)
    else:
        return bs(x, m+1, h)

for i in b:
    print(bs(i, 0, n-1), end = ' ')
