import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
q, r = divmod(n, 2)
print(a[q+r-1])
