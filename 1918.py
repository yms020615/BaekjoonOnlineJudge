import sys
input = sys.stdin.readline

infix = input().rstrip()

def icp(op):
    if op == '(':
        return 0
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 3
    if op == '#':
        return 8
    return

def isp(op):
    if op == '(':
        return 8
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 3
    return

postfix = ''
stack = []
for c in infix:
    if c == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    elif c == '+' or c == '-' or c == '*' or c == '/':
        while stack and isp(stack[-1]) <= icp(c):
            postfix += stack.pop()
        stack.append(c)
    elif c == '(':
        stack.append(c)
    else:
        postfix += c

while stack:
    postfix += stack.pop()

print(postfix)
