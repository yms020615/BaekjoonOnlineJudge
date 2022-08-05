import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(1)
    exit(0)

dic = {}
for i in range(len(a)):
    dic[a[i]] = i
m = sorted(a)

def selection_sort_odd(a):
    for i in range(n-1, 0, -1):
        maxn = m.pop()
        maxid = dic[maxn]

        if i != maxid:
            a[i], a[maxid] = a[maxid], a[i]
            dic[a[maxid]] = dic[maxn]
            del dic[maxn]
            
        left, right = 0, n-1
        check = 0
        while True:
            if left > right:
                break

            if a[left] == b[left]:
                left += 1
                if a[right] == b[right]:
                    right -= 1
                else:
                    break
            else:
                break
            check += 1

            if check > n // 2:
                print(1)
                exit(0)

def selection_sort_even(a):
    for i in range(n-1, 0, -1):
        maxn = m.pop()
        maxid = dic[maxn]

        if i != maxid:
            a[i], a[maxid] = a[maxid], a[i]
            dic[a[maxid]] = dic[maxn]
            del dic[maxn]
            
        left, right = 0, n-1
        check = 0
        while True:
            if left > right:
                break

            if a[left] == b[left]:
                left += 1
                if a[right] == b[right]:
                    right -= 1
                else:
                    break
            else:
                break
            check += 1

            if check >= n // 2:
                print(1)
                exit(0)

if n % 2:
    selection_sort_odd(a)
else:
    selection_sort_even(a)
print(0)
