a, b = map(int, input().split())
c = (a % 10) * 100 + ((a // 10) % 10) * 10 + a // 100
d = (b % 10) * 100 + ((b // 10) % 10) * 10 + b // 100
if c > d:
    print(c)
else: print(d)
