import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0: return x;
    return gcd(y, x%y)

n = int(input())
a = list(map(int, input().split()))
for i in range(1, len(a)):
    y, x = a[0], a[i]
    print('{}/{}'.format(y//gcd(max(x,y),min(x,y)), x//(gcd(max(x,y),min(x,y)))))
