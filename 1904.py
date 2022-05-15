import sys
input = sys.stdin.readline

n = int(input())

fib = [1] + [1]

for i in range(2, n+1):
    fib.append((fib[i-2] + fib[i-1]) % 15746)

print(fib[-1] % 15746)
