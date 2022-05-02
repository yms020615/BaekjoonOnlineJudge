import sys
input = sys.stdin.readline

min, max = map(int, input().split())
count = 0
a = [1 for _ in range(min, max + 1)]
square = [i ** 2 for i in range(2, int(max ** 0.5) + 1)]

for i in square:
    n = min // i
    for j in range(n, max):
        if i * j - min >= 0 and i * j <= max:
            a[i * j - min] = 0
        if i * j > max:
            break
print(sum(a))
