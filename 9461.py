import sys
input = sys.stdin.readline

a = [1, 1, 1, 2, 2]
b = []
for i in range(int(input())):
    b.append(int(input()))
c = max(b)
for j in range(5, c+1):
    a.append(a[j-5]+a[j-4]+a[j-3])
for i in b:
    print(a[i-1])
