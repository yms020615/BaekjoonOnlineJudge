import sys
input = sys.stdin.readline

cnt1 = 0
cnt2 = 0

def cut(x, y, n):
    global cnt1
    global cnt2

    c = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if c != p[i][j]:
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    if c == 0:
        cnt1 += 1
    else:
        cnt2 += 1

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

cut(0, 0, n)
print(cnt1)
print(cnt2)
