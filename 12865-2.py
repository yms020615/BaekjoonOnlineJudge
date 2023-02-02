n, k = map(int, input().split())

w, v = [0], [0]
for _ in range(n):
    tmp1, tmp2 = map(int, input().split())
    w.append(tmp1)
    v.append(tmp2)
    
F = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(len(F)):
    F[i][0] = 0
for i in range(len(F[0])):
    F[0][i] = 0

def Knapsack(i, j):
    if i == 0:
        return F[0][j]
    
    if F[i][j] < 0:
        if j < w[i]:
            value = Knapsack(i - 1, j)
        else:
            value = max(Knapsack(i - 1, j),
                    v[i] + Knapsack(i - 1, j - w[i]))
        F[i][j] = value
    return F[i][j]
    
Knapsack(n, k)
print(F[-1][-1])
