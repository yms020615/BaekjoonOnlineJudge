import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(1)
    exit(0)

def selection_sort_even(a):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

                check = 1
                id = 0
                mid = n // 2
                while check:
                    if a[id] == b[id]:
                        if id == n-1:
                            print(1)
                            exit(0)

                        if id < mid:
                            id += mid
                        else:
                            id -= mid - 1
                    else:
                        check = 0

def selection_sort_odd(a):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

                check = 1
                id = 0
                mid = n // 2
                while check:
                    if a[id] == b[id]:
                        if id == n-2:
                            print(1)
                            exit(0)

                        if id <= mid:
                            id += mid
                        else:
                            id -= mid - 1
                    else:
                        check = 0

if n % 2:
    selection_sort_odd(a)
else:
    selection_sort_even(a)
print(0)
