import sys
c = []
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    c.append([b, a])
c.sort()
for i in range(len(c)):
    print(c[i][1], c[i][0])
