n = int(input())
a = list(map(int, input().split()))
k = 0
for i in a:
    for j in range(2, i):
        if i % j == 0:
            k += 1
            break
if 1 in a: print(n - k - 1)
else: print(n - k)
