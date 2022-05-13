import sys
sys.setrecursionlimit(1000000)

t = input()
p = input()

table = [0] * len(p)
def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

F = failure(p, table)
find = 0
f = []
def kmp(i, j):
    global find
    for i in range(len(t)):
        if j > 0 and t[i] != p[j]:
            j = F[j-1]
        if t[i] == p[j]:
            if j == len(p)-1:
                find += 1
                f.append(i-j+1)
                j = F[j]
            else:
                j += 1

kmp(0, 0)
print(find)
for i in f:
    print(i, end=' ')
