import sys
input = sys.stdin.readline

n = int(input())
x = []
y = []
for _ in range(n):
    x_input, y_input = map(int, input().split())
    x.append(x_input)
    y.append(y_input)

a = 0
for i in range(n-1):
        a += x[i] * y[i+1]
a += x[n-1] * y[0]
for i in range(n-1):
        a -= x[i+1] * y[i]
a -= x[0] * y[n-1]
a /= 2
print(round(abs(a), 1))
