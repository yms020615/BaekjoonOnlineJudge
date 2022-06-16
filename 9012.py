import sys
input = sys.stdin.readline

for i in range(int(input())):
    a = input()
    b = list(str(a))
    k = 0
    for i in range(len(b)):
        if b[i] == '(': k += 1
        elif b[i] == ')': k -= 1
        if k < 0: break
    if k == 0: print('YES')
    else: print('NO')
