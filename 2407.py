import sys
input = sys.stdin.readline

n, r = map(int, input().split())
c = [[0] * 101 for _ in range(101)]

for i in range(n+1):
    for j in range(r+1):
        if i == j or j == 0:
            c[i][j] = 1
        else:
            c[i][j] = c[i-1][j] + c[i-1][j-1]
print(c[n][r])
