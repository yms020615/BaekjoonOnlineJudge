n = int(input())
k = 0
for i in range(n):
    m = sum(map(int, str(i)))
    if i+m == n:
        print(i)
        k = 1
        break
if k == 0: print(0)
