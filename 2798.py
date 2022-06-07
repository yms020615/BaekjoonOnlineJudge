a, b = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
d = c[0] + c[1] + c[2]
for i in c:
    for j in c:
        for k in c:
            if i != j and i != k and j != k:
                if b - d > b - (i+j+k):
                    if b - (i+j+k) >= 0:
                        d = i+j+k
print(d)
