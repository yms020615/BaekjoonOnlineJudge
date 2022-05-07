import sys
input = sys.stdin.readline

a = list(input().strip('\n'))
b = []
k = len(a)
for i in range(int(input())):
    s = input().split()
    if s[0] == 'L':
        if a: b.append(a.pop())
    elif s[0] == 'D':
        if b: a.append(b.pop())
    elif s[0] == 'B':
        if a: a.pop()
    elif s[0] == 'P':
        a.append(s[1])
print(''.join(a + list(reversed(b))))
