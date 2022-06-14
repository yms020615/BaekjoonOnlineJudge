import sys
input = sys.stdin.readline

a = [False, False] + [True] * 1000000

for i in range(2, 1001):
    if a[i] == True:
        for j in range(2*i, 1000001, i):
            a[j] = False

while True:
    n = int(input())

    if n == 0: break

    x, y = 2, n-2
    for i in range(1000000):
        if a[x] and a[y]:
            print(f'{n} = {x} + {y}')
            break
        x += 1
        y -= 1

    else: print("Goldbach's conjecture is wrong.")
