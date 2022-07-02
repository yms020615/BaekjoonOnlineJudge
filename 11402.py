import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())

def conv(n, q):
    c = []

    while n > 0:
        n, mod = divmod(n, q)
        c.append(mod)

    return c

n_m = conv(n, m)
k_m = conv(k, m)

for i in range(len(k_m), len(n_m)):
    k_m.append(0)

max = max(n_m)

comb = [[0 for _ in range(max+1)] for _ in range(max+1)]
for i in range(max+1):
    for j in range(max+1):
        if i == j or j == 0:
            comb[i][j] = 1
        else:
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

lucas = 1
for i in range(len(n_m)):
    if n_m[i] < k_m[i]:
        lucas *= 0
        break
    else:
        lucas *= comb[n_m[i]][k_m[i]]
        lucas %= m

print(lucas % m)
