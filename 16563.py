import sys
input = sys.stdin.readline

minf = [0 for _ in range(5000001)]

def f(n):
    while n > 1:
        print(minf[n], end = ' ')
        n //= minf[n]
    print()

def erat():
    minf[0] = minf[1] = -1
    for i in range(2, 5000001):
        minf[i] = i

    for i in range(2, int(5000001 ** 0.5) + 1):
        if minf[i] == i:
            for j in range(i * i, 5000001, i):
                if minf[j] == j:
                    minf[j] = i

k = int(input())
l = list(map(int, input().split()))
erat()

for n in l:
    f(n)
