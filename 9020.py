def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    n = int(input())
    k = 0
    while True:
        if is_prime(n//2 - k) and is_prime(n//2 + k) is True:
            print(n//2 - k, n//2 + k)
            break
        else: k+=1
