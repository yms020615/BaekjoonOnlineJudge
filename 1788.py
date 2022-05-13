import sys
input = sys.stdin.readline

n = int(input())
fib = []
if n > 0:
    print(1)
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-2] + fib[i-1]) % 1000000000)
    print(fib[n] % 1000000000)

elif n == 0:
    print('0\n0')

elif n < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
    fib = [0, 1]
    for i in range(2, -n + 1):
        fib.append((fib[i-2] + fib[i-1]) % 1000000000)
    print(fib[-n] % 1000000000)
