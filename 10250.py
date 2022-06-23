for i in range(int(input())):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h + 1
    if a == 0:
        print(h * 100 + b - 1)
    else:
        print(a * 100 + b)
