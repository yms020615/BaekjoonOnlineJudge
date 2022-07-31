import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = {}
for _ in range(n):
    s = input().split()
    a[s[0]] = s[1]
for _ in range(m):
    s = input().strip('\n')
    print(a[s])
