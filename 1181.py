import sys
c = []
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip('\n')
    c.append([len(s), s])
c.sort()
s = []
for i in range(1, c[-1][0]+1):
    for j in range(len(c)):
        if c[j][0] == i and c[j][1] not in s:
            s.append(c[j][1])
for i in s:
    print(i)
