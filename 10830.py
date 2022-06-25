import sys
input = sys.stdin.readline

c = 1000
n, b = map(int, input().split())

def multiply(mat1, mat2, n):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(n)) % c

    return ans

def power(mat, p):
    if p == 1:
        return mat
    else:
        temp = power(mat, p // 2)
        if p % 2 == 0:
            return multiply(temp, temp, n)
        else:
            return multiply(multiply(temp, temp, n), mat, n)

m = []
for i in range(n):
    m.append(list(map(int, input().split())))
p = power(m, b)
for i in p:
    for j in i:
        print(j % c, end=' ')
    print()
