import sys
input = sys.stdin.readline

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
a = ''
b = int(b)
n = list(reversed(n))
k = 0
for i in range(len(n)):
    k += s.index(n[i]) * (b ** i)
print(k)
