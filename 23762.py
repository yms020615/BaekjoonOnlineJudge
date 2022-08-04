input = __import__('sys').stdin.readline

n = int(input())
m = list(map(int, input().split()))

m = list(enumerate(m))
m.sort(key = lambda x: x[1])

minDiff = [0 for _ in range(n)]
missIndex = [[] for _ in range(n)]

for i in range(3):
    for j in range(i + 1):
        missIndex[i].append(m[j][0])

for i in range(3, n):
    diff = m[i][1] - m[i - 3][1]

    if (i + 1) % 4:
        minDiff[i] = min(minDiff[i - 1], minDiff[i - 4] + diff)

        if minDiff[i] == minDiff[i - 1]:
            for j in missIndex[i - 1]:
                missIndex[i].append(j)
            missIndex[i].append(m[i][0])
        else:
            for j in missIndex[i - 4]:
                missIndex[i].append(j)

    else:
        minDiff[i] = minDiff[i - 4] + diff

print(minDiff[n - 1])
for i in missIndex[n - 1]:
        print(i)
