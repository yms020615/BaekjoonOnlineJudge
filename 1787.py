import sys
input = sys.stdin.readline

n = int(input())
p = input().rstrip()
table = [0 for _ in range(n)]

def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

failure(p, table)

ans = 0
for i in range(1, n + 1):
    if table[i - 1]:
        if table[table[i - 1] - 1]:
            table[i - 1] = table[table[i - 1] - 1]
        
        ans += i - table[i - 1]

print(ans)
