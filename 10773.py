import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    n = int(input())
    if n == 0 and stack: stack.pop()
    else: stack.append(n)
print(sum(stack))
