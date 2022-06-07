import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = a.copy(); b.sort()
c = a.copy(); c.sort(reverse=True)
if a == b: print('ascending')
elif a == c: print('descending')
else: print('mixed')
