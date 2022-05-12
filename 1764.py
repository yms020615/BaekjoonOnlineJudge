import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input().strip('\n'))
for _ in range(m):
    b.add(input().strip('\n'))
c = a & b
print(len(c))
for i in sorted(c):
    print(i)
