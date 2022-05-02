import sys
input = sys.stdin.readline

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

n = int(input())
a = list(map(int, input().split()))
b = [0] * n

for i in range(n):
    e = -1000000000
    for j in range(i+1, n):
        if slope(i, a[i], j, a[j]) > e:
            e = slope(i, a[i], j, a[j])
            b[i] += 1
            b[j] += 1

print(max(b))
