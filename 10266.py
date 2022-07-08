input = __import__('sys').stdin.readline

t = [0 for _ in range(720000)]
p = [0 for _ in range(360000)]

n = int(input())
clock = list(map(int, input().split()))
pattern = list(map(int, input().split()))

for i in clock:
    t[i], t[i + 360000]= 1, 1

for i in pattern:
    p[i] = 1

table = [0 for _ in range(360000)]
def failure(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

failure(p, table)
            
def kmp(i, j):
    for i in range(len(t)):
        if j > 0 and t[i] != p[j]:
            j = table[j - 1]
        if t[i] == p[j]:
            if j == len(p) - 1:
                return 'possible'
            else:
                j += 1
    return 'impossible'

print(kmp(0, 0))
