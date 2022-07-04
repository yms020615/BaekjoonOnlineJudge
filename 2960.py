input = __import__('sys').stdin.readline

n, k = map(int, input().split())

count = 0
sieve = [False, False] + [True] * n

for i in range(2, n + 1):
    if not sieve[i]:
        continue

    for j in range(i, n + 1, i):
        if sieve[j]:
            sieve[j] = False
            count += 1
        if k == count:
            print(j)
            exit(0)
