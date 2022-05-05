m = int(input())
n = 0
for i in range(m):
    a = input()
    b = list(a)
    c = [0 for i in range(101)]
    j, k = 0, 0
    for i in range(1, len(b)):
        if b[i - 1] != b[i]:
            c[j] = b[i - 1]
            j += 1
        c[j] = b[i]
    for i in range(len(c)):
        for j in range(len(c)):
          if c[i] == c[j] and c[i] != 0 and i != j:
              k += 1
              break
    if k != 0:
        n += 1
print(m - n)
