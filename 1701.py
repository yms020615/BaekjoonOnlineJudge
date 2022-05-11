import sys
input = sys.stdin.readline

p = input().rstrip()

def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

ans = 0
for i in range(len(p)):
    table = [0] * (len(p) - i)
    failure(p[i:], table)
    ans = max(ans, max(table))
print(ans if ans > 1 else 0)
