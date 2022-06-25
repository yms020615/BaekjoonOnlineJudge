import sys
input = sys.stdin.readline

from collections import deque
a = deque()

for i in range(int(input())):
    s = list(map(str, input().split()))
    if s[0] == 'push_front':
        a.appendleft(s[1])
    elif s[0] == 'push_back':
        a.append(s[1])
    elif s[0] == 'pop_front':
        if a: print(a.popleft())
        else: print(-1)
    elif s[0] == 'pop_back':
        if a: print(a.pop())
        else: print(-1)
    elif s[0] == 'size':
        print(len(a))
    elif s[0] == 'empty':
        if a: print(0)
        else: print(1)
    elif s[0] == 'front':
        if a: print(a[0])
        else: print(-1)
    elif s[0] == 'back':
        if a: print(a[-1])
        else: print(-1)
