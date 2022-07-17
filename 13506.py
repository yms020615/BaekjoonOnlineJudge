t = input().rstrip()

table = [0] * len(t)
table2 = table[1:-2]
def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

F = failure(t, table)
k = table[-1]
while k > 0:
    for i in range(1, len(t) - 1):
        if table[i] == k:
            print(t[:k])
            exit(0)
    k = table[k - 1]

print(-1)
