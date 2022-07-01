import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

def combination(n, k):
    return factorial(n)/ factorial(k) / factorial(n - k)

n, k = map(int, input().split())
print(int(combination(n, k)))
