for i in range(int(input())):
    n, a = input().split()
    b = [' ' for i in range(len(a))]
    for i in range(len(a)):
        b[i] = a[i] * int(n)
    for i in b:
        print(i, end='')
    print()
