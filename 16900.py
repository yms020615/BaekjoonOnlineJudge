import sys
input = sys.stdin.readline

s, k = input().split()
k = int(k)

table = [0] * len(s)
def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

F = failure(s, table)
print(len(s) * k - F[-1] * (k-1))
