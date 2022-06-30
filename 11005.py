import sys
input = sys.stdin.readline

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
a = ''

while n:
    a += str(s[n%b])
    n //= b
print(a[::-1])
