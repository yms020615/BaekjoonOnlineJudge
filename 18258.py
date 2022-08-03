import sys
input = sys.stdin.readline

from collections import deque

def size(a):
        return len(a)
def empty(a):
        if len(a) == 0: return 1
        else: return 0
def top(a):
        if len(a) == 0: return -1
        else: return a[-1]
def pop(a):
        if len(a) == 0: return -1
        else: return a.popleft()
def push(a, n):
        a.append(n)
def front(a):
        if len(a) == 0: return -1
        else: return a[0]
def back(a):
        if len(a) == 0: return -1
        else: return a[-1]

stack = deque([])
for i in range(int(input())):
    a = input().split()
    if a[0] == 'size':
        print(size(stack))
    elif a[0] == 'empty':
        print(empty(stack))
    elif a[0] == 'top':
        print(top(stack))
    elif a[0] == 'pop':
        print(pop(stack))
    elif a[0] == 'push':
        push(stack, a[1])
    elif a[0] == 'front':
        print(front(stack))
    elif a[0] == 'back':
        print(back(stack))
