import sys
n = int(sys.stdin.readline())
a = map(int, str(n))
b = []
for i in a:
    b.append(i)
b.sort(reverse=True)
for i in b:
    print(i, end='')
