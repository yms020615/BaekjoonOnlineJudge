import sys
input = sys.stdin.readline

l = int(input())
p = input().strip()
table = [0] * l
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
print(l - F[-1])
