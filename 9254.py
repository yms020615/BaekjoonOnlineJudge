import sys
input = sys.stdin.readline

def gauss(mat, x):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue

            try:
                m = 1 / mat[i][i]
            except:
                print('no inverse')
                exit(0)
            for k in range(2 * n):
                mat[i][k] *= m

            if mat[j][i]:
                m = -mat[j][i] / mat[i][i]
                for k in range(2 * n):
                    mat[j][k] += m * mat[i][k]

n = int(input())

mat1 = []
for i in range(n):
    mat1.append(list(map(int, input().split())))
    for _ in range(n):
        mat1[i].append(0)
    mat1[i][i+n] = 1
mat1.sort(key = lambda x: abs(x[0]), reverse = True)

gauss(mat1, n)
for i in mat1:
    print(*i[n:])
