import sys
input = sys.stdin.readline

def gauss(mat, x):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue

            m = 1 / mat[i][i]
            for k in range(n+1):
                mat[i][k] *= m

            if mat[j][i]:
                m = -mat[j][i] / mat[i][i]
                for k in range(n+1):
                    mat[j][k] += m * mat[i][k]

n = int(input())

mat1 = []
for i in range(n):
    mat1.append(list(map(int, input().split())))
mat1.sort(key = lambda x: abs(x[0]), reverse = True)

gauss(mat1, n)
for i in mat1:
    print(round(i[-1]), end = ' ')
