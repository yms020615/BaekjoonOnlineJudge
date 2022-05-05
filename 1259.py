import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break
    k = n
    temp = 0
    while n > 0:
        temp = n % 10 + temp * 10
        n //= 10
    if temp == k: print('yes')
    else: print('no')
