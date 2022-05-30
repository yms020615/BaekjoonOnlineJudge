def func(x, y, n):
    if n == 1:
        a[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                func(x + n // 3 * i, y + n // 3 * j, n // 3)

n = int(input())
a = [[' '] * n for i in range(n)]
func(0, 0, n)

for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()
