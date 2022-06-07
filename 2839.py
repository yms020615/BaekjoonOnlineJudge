a = int(input())
n = 0
while a >= 0:
    if a % 5 == 0:
        n += a // 5
        print(n)
        break
    a -= 3
    n += 1
else:
    print(-1)
