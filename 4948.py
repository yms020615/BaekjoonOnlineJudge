def prime(a):
    k = 0
    for i in range(a+1, 2*a+1):
        if i==2: k+=1; continue
        for j in range(2, int(i**0.5)+1):
            if i%j==0: k+=1; break
    if a==1: print(1)
    else: print(a-k)

while True:
    a = int(input())
    if a==0: break
    prime(a)
