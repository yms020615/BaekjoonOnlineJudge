def f(n):
    if n==0: return 0
    elif n==1 or n==2: return 1
    else: return f(n-1)+f(n-2)

print(f(int(input())))
