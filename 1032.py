import sys
input = sys.stdin.readline

a = []
b = []
n = int(input())
for i in range(n):
    a.append(list(map(str, input())))
for i in range(len(a[0])):
    temp = True
    for j in range(n):
        for k in range(j+1, n):
            if a[j][i] != a[k][i]:
                temp = False
                break
    if temp == True:
        b.append(a[0][i])
    elif temp == False:
        b.append('?')
for i in b:
    print(i, end='')
