import sys
input = sys.stdin.readline

a = [1, 2, 4]
for i in range(3, 10):
    a.append(a[i-1] + a[i-2] + a[i-3])
for i in range(int(input())):
    n = int(input())
    print(a[n-1])
