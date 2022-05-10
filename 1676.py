import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

x = int(input())
i = 0
while factorial(x) % (10 ** i) == 0:
    i += 1
print(i - 1)
