a, b = map(int, input().split())
for i in range(a, b+1):
    if i == 1:
        continue
    k = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            k += 1
            break
    if k == 0:
        print(i)
