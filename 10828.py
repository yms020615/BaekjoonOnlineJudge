import sys
input = sys.stdin.readline

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
        else: return a.pop(-1)
def push(a, n):
        a.append(n)

stack = []
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
