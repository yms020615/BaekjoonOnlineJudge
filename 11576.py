import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
x = list(map(int, input().split()))
k = 0
for i in range(m):
    k += x[-1-i] * (a ** i)
c = []
while k > 0:
    c.append(k % b)
    k //= b
for i in c[-1::-1]:
    print(i, end=' ')
