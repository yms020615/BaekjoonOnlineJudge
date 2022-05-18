import sys
input = sys.stdin.readline

c = 1000000000

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

m = [[1, 1], [1, 0]]
a, b = map(int, input().split())
print((power(m, b+2)[0][1] - power(m, a+1)[0][1]) % c)
