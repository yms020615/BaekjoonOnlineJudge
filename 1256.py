import sys
input = sys.stdin.readline

from itertools import *

n, m, k = map(int, input().split())
word = [[1] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        word[i][j] = word[i-1][j] + word[i][j-1]

if word[n][m] < k:
    print(-1)
else:
    ans = ''
    while True:
        if n == 0 or m == 0:
            ans += 'z' * m
            ans += 'a' * n
            break

        temp = word[n-1][m]
        if k <= temp:
            ans += 'a'
            n -= 1
        else:
            ans += 'z'
            m -= 1
            k -= temp
    print(ans)
