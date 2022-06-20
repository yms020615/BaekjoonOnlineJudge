import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    p, q = map(int, input().split())
    fib = [0, 1]
    for j in range(2, p+1):
        fib.append((fib[j-2] + fib[j-1]) % q)
    print('Case #{}: {}'.format(i+1, fib[p] % q))
