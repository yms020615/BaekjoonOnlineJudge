import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = {}
b = []
for i in range(n):
    s = input().strip('\n')
    a[s] = i+1
    b.append(s)
for _ in range(m):
    s = input().strip('\n')
    if s.isdigit():
        print(b[int(s)-1])
    else:
        print(a[s])
