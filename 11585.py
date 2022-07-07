n = int(input())
p = input().rstrip().split()
t = input().rstrip().split()

if n == 1 or sorted(p)[0] == sorted(p)[-1]:
    print('1/1')
    exit(0)

t += t[:-1]

table = [0] * n
def failure(p, table):
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
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
            j = F[j - 1]
        if t[i] == p[j]:
            if j == n - 1:
                find += 1
                f.append(i - j + 1)
                j = F[j]
            else:
                j += 1

kmp(0, 0)
from fractions import Fraction
print(Fraction(len(f), n))
