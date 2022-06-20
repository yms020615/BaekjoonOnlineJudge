import sys
input = sys.stdin.readline

a = list(input().strip('\n'))
b = list(input().strip('\n'))
s = []

for i in a:
    s.append(i)

    if i == b[-1]:
        if s[-len(b):] == b:
            del s[-len(b):]

if s:
    print(''.join(s))
else:
    print('FRULA')
