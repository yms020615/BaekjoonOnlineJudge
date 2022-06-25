import sys
c = []
for i in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    c.append([a, b])
c.sort(key = lambda a : int(a[0]))
for i in range(len(c)):
    print(c[i][0], c[i][1])
