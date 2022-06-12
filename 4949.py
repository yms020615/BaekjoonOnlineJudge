import sys
input = sys.stdin.readline

while True:
    a = input().strip('\n')
    if a[0] == '.' and len(a) == 1: break
    stack = []
    temp = True
    for i in a:
        try:
            if i == '(' or i == '[': stack.append(i)
            
            elif i == ')':
                if stack[-1] == '[' or not stack:
                    temp = False
                elif stack[-1] == '(': stack.pop()
            
            elif i == ']':
                if stack[-1] == '(' or not stack:
                    temp = False
                elif stack[-1] == '[':
                    stack.pop()
        except:
            temp = False
    if temp and not stack: print('yes')
    else: print('no')
