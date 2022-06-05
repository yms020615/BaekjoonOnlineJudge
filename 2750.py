a = []
for i in range(int(input())):
    a.append(int(input()))
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
for i in a:
    print(i)
