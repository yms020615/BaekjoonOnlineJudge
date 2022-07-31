import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        mod = b
        b = a%b
        a = mod
    return a

N, S = map(int, input().split())
a = list(map(int, input().split()))
b = list(set(abs(a[i]-S) for i in range(N)))
d = min(b)
for i in range(len(b)):
    d = gcd(b[i], d)
print(d)
