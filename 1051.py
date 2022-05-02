import sys
input = sys.stdin.readline

a, b = map(int, input().split())
s = []
p = []
for i in range(a):
    s.append(list(map(int, input().strip('\n'))))
for k in range(1, min(a, b)):
    for i in range(a - k):
        for j in range(b - k):
            if i + k < a and j + k < b:
                if s[i][j] == s[i+k][j] == s[i][j+k] == s[i+k][j+k]:
                    p.append(k + 1)
if p: print(max(p) ** 2)
else: print(1)
