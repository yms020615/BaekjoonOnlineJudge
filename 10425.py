import sys
input = sys.stdin.readline

t = int(input())
n = []
fib = {0: 0, 1: 1}
f1, f2 = 1, 0
for i in range(2, 100001):
    temp = str(f1 + f2)[-21:]
    fib[temp] = i
    f2 = f1
    f1 = int(temp)

for _ in range(t):
    print(fib[input().strip()[-21:]])
