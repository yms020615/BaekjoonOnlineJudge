import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lan = [int(input()) for _ in range(a)]
start, end = 1, max(lan)

while start <= end:
    middle = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // middle
    if lines >= b:
        start = middle + 1
    else:
        end = middle - 1
print(end)
