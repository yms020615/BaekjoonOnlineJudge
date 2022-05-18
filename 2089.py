import sys
input = sys.stdin.readline

n = int(input())
a = ''
if not n: print(0, end='')
while n:
    if n % -2:
        a = '1' + a
        n = n // -2 + 1
    else:
        a = '0' + a
        n //= -2
print(a)
