import sys
input = sys.stdin.readline

a = []
b = []
k = 1
temp = True
for i in range(int(input())):
    n = int(input())
    while k <= n:
        a.append(k)
        b.append('+')
        k += 1
    if a[-1] == n:
        a.pop()
        b.append('-')
    else: temp = False; break
if not temp: print('NO')
else:
    for i in b:
        print(i)
