import sys
input = sys.stdin.readline

a, b = map(int, input().split())
q = [i for i in range(1, a+1)]
josephus = []
n = b
for i in range(a):
    josephus.append(n)
    q[n-1] = -1
    if len(josephus) == a:
        break
    for j in range(b):
        n += 1
        if n > a:
            n -= a
        while q[n-1] == -1:
            n += 1
            if n > a:
                n -= a

print('<', end='')
for i in josephus:
    if i == josephus[-1]:
        print('{}'.format(i), end='')
    else:
        print('{},'.format(i), end=' ')
print('>')
