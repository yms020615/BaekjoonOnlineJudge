def factorization(x):
    d = 2
    p = []

    while d <= x:
        if x % d == 0:
            p.append(d)
            x //= d
        else:
            d = d + 1

    return p

from collections import Counter

while True: 
    try:
        s = input().rstrip().split('/')
        n = int(s[1])

        p = Counter(factorization(n))
        ans = 1
        for k, v in p.items():
            ans *= (2 * v) + 1

        print((ans // 2) + 1)

    except:
        exit(0)
