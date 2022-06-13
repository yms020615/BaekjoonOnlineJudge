import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    try:
        l = deque(list(map(int, input().rstrip()[1:-1].split(','))))
    except:
        l = []
    r = False
    for i in p:
        if i == 'R':
            if r:
                r = False
            else:
                r = True
        if i == 'D':
            try:
                if r:
                    l.pop()
                    n -= 1
                else:
                    l.popleft()
                    n -= 1
            except:
                print('error')
                n -= 1
                break

    if n > 0:
        if r:
            print('[', end = '')
            for i in range(n-1, 0, -1):
                print(l[i], end = ',')
            print('%d]' % l[0])
        else:
            print('[', end = '')
            for i in range(n-1):
                print(l[i], end = ',')
            print('%d]' % l[-1])
    elif n == 0:
        print('[]')
