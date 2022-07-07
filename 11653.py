def factoring(n):
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            k = n // i
            break
    if k > 1: return factoring(k)

a = int(input())
if a == 1: print()
elif a > 1: factoring(a)
