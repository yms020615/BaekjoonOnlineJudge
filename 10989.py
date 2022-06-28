import sys
a = [0] * 10001
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    a[n] += 1
for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)
