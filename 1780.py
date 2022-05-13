import sys
input = sys.stdin.readline

p1, p2, p3 = 0, 0, 0
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

def cut(x, y, n):
    global p1, p2, p3

    temp = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != temp:
                for k in range(3):
                    for l in range(3):
                        cut(x+k*n//3, y+l*n//3, n//3)
                return

    if temp == -1:
        p1 += 1
    elif temp == 0:
        p2 += 1
    elif temp == 1: 
        p3 += 1

cut(0, 0, n)
print(p1)
print(p2)
print(p3)
