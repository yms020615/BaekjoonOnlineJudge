a = int(input())
b = int(input())
c = 0
sum = 0
for i in range(a, b+1):
    if i == 1:
        continue
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
            break
    if k == 0 and c == 0:
        c = i
    if k == 0:
        sum += i
if sum == 0: print(-1)
else: print('{}\n{}'.format(sum, c))
