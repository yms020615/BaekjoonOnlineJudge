a = int(input())
n = 0
while n*(n-1)/2 < (a-1)/6:
    n += 1
if a==1: print(1)
else: print(n)
