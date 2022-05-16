import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            s[i][j] = s[i][j] + s[i-1][j]
        elif i == j:
            s[i][j] = s[i][j] + s[i-1][j-1]
        else:
            s[i][j] = max(s[i][j] + s[i-1][j], s[i][j] + s[i-1][j-1])
print(max(s[n-1]))
