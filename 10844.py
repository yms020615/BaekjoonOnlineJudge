import sys
input = sys.stdin.readline

n = int(input())
a = [[0] * 10 for i in range(101)]
a[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            a[i][j] = a[i-1][j+1] % 1000000000
        elif j == 9:
            a[i][j] = a[i-1][j-1] % 1000000000
        else:
            a[i][j] = (a[i-1][j-1] + a[i-1][j+1]) % 1000000000
print(sum(a[n]) % 1000000000)
