n = int(input())

erat = [True] * 1000001
erat[0], erat[1] = False, False

def eratos():
    for i in range(2, int(1000001 ** 0.5) + 1):
        if erat[i]:
            for j in range(2 * i, 1000001, i):
                erat[j] = False
    return [i for i in range(n, 1000001) if erat[i]]

prime = eratos()
t = True
for i in prime:
    if str(i) == str(i)[::-1]:
        print(i)
        t = False
        break

if t:
    print(1003001)
