a = [i+1 for i in range(10000)]
b = []

for i in range(1, 10000):
    x = i % 10
    y = (i // 10) % 10
    z = (i // 100) % 10
    w = i // 1000
    b.append(i + x + y + z + w)

for i in b:
    if i < 10000 and i in a:
        a.remove(i)

a.remove(10000)

for i in a:
    print(i)
