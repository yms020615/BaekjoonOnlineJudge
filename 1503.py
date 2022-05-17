input = __import__('sys').stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split())) if m else []
a = [i for i in range(1, 1002)]
for i in s:
    a.remove(i)

ans = 99999999999
for i in a:
    for j in a:
        for k in a:
            ans = min(ans, abs(n - i * j * k))

print(ans)
