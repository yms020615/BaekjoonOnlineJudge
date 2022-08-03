import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
a = []
for i in range(n):
    k = map(int, input().split())
    for j in k:
        a.append(j)
max = max(a)
min = min(a)

mintime = 9223372036854775807
height = 0
for i in range(min, max+1):
    time1, time2, block = 0, 0, 0
    for j in a:
        if j < i:
            time1 += i - j
        else:
            time2 += 2 * (j - i)
    if time1 > time2 // 2 + b:
        continue
    time = time1 + time2
    if mintime >= time:
        mintime = time
        height = i
print(mintime, height)
