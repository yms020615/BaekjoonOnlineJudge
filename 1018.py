def func(x, y):
    n = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if (i+j)%2==0:
                if s[i][j] == 'W': n += 1
            elif (i+j)%2==1:
                if s[i][j] == 'B': n += 1
    return min(n, (64 - n))

n, m = map(int, input().split())
a = [0 for i in range(60)]
s = [[0 for i in range(60)] for i in range(60)]
for i in range(n):
    a = input()
    s[i] = list(a) + [0] * 60
k = 64
for i in range(m-7):
    for j in range(n-7):
        if k > func(i, j):
            k = func(i, j)
print(k)
