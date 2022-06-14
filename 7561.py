import sys
input = sys.stdin.readline

def gauss(mat, x):
    n = len(mat)
    for i in range(3):
        for j in range(3):
            if j == i:
                continue

            m = 1 / mat[i][i]
            for k in range(4):
                mat[i][k] *= m

            if mat[j][i]:
                m = -mat[j][i] / mat[i][i]
                for k in range(4):
                    mat[j][k] += m * mat[i][k]

n = int(input())

for _ in range(n):
    m = []
    for i in range(3):
        m.append(list(map(int, input().split())))
    l = []
    l.append(m[0][3] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
          - m[0][1] * (m[1][3] * m[2][2] - m[1][2] * m[2][3])
          + m[0][2] * (m[1][3] * m[2][1] - m[1][1] * m[2][3]))
    l.append(m[0][0] * (m[1][3] * m[2][2] - m[1][2] * m[2][3])
          - m[0][3] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
          + m[0][2] * (m[1][0] * m[2][3] - m[1][3] * m[2][0]))
    l.append(m[0][0] * (m[1][1] * m[2][3] - m[1][3] * m[2][1])
          - m[0][1] * (m[1][0] * m[2][3] - m[1][3] * m[2][0])
          + m[0][3] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    l.append(m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
          - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
          + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    print(*l)

    if l[3]:
        print('Unique solution: ', end = '')
        m.sort(key = lambda x: abs(x[0]), reverse = True)
        gauss(m, 3)
        for i in m:
            if -0.0005 < i[3] < 0.0005:
                i[3] = 0
        print('%.3f %.3f %.3f' % (m[0][3], m[1][3], m[2][3]))
        print('')
    else:
        print('No unique solution')
        print('')
    
