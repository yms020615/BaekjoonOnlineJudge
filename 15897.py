import sys
input = sys.stdin.readline

n = int(input())
i = n
n -= 1
ans = 0
while i:
    ans += (n // i + 1) * (i - (n // ((n // i) + 1)))
    i = n // ((n // i) + 1)
print(ans)
