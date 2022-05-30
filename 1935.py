input = __import__('sys').stdin.readline

n = int(input())
op = input().rstrip()
num = [float(input()) for _ in range(n)]
ops = '+-*/'
stack = []
temp1, temp2 = 0.0, 0.0

for i in op:
    if i in ops:
        temp1 = stack.pop()
        temp2 = stack.pop()
        if i == '+':
            stack.append(temp2 + temp1)
        elif i == '-':
            stack.append(temp2 - temp1)
        elif i == '*':
            stack.append(temp2 * temp1)
        elif i == '/':
            stack.append(temp2 / temp1)
    else:
        stack.append(num[ord(i) - ord('A')])

print('%.2f' % stack[0])
