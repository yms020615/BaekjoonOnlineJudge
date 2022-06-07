import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
start, end = 1, max(a)

while start <= end:
    middle = (start + end) // 2
    sum = 0

    for i in a:
        if i > middle:
            sum += i - middle

    if sum >= m:
        start = middle + 1
    else:
        end = middle - 1
print(end)
