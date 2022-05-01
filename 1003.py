import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    zero, one, temp = 1, 0, 0
    for _ in range(n):
        temp = one
        one += zero
        zero = temp
    print(zero, one)
