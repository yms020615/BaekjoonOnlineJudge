for i in range(int(input())):
    a = int(input())
    b = int(input())
    c = [i for i in range(1, 15)]
    d = [i for i in range(1, 15)]
    for k in range(a):
        for j in range(13):
            c[j] = sum(d[0:j+1])
        c[13] = sum(d)
        d = c.copy()
    print(c[b-1])
