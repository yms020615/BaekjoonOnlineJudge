import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

c = 10000

def multiply(mat1, mat2):
    ans = [[0, 0], [0, 0]]
    ans[0][0] = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % c
    ans[0][1] = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % c
    ans[1][0] = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % c
    ans[1][1] = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % c
    return ans

def power(mat, p):
    if p == 1:
        return mat
    else:
        temp = power(mat, p // 2)
        if p % 2 == 0:
            return multiply(temp, temp)
        else:
            return multiply(multiply(temp, temp), mat)

while True:
    n = int(input())
    if n == 0:
        print(0)
        continue
    if n == -1:
        break
    m = [[1, 1], [1, 0]]
    print(power(m, n)[0][1] % c)
