input = __import__('sys').stdin.readline

n = 1000 - int(input())

a = [500, 100, 50, 10, 5, 1]

i = 0
ans = 0
while n:
    ans += n // a[i]
    n %= a[i]
    i += 1

print(ans)
