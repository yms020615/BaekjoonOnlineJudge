import sys
input = sys.stdin.readline

for i in range(int(input())):
    a = input()
    b = list(map(str, a.split()))
    for i in b:
        k = list(str(i))
        for j in reversed(k):
            print(j, end='')
        print(' ', end='')
