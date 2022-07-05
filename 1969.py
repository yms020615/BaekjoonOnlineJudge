input = __import__('sys').stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]

ans = ['X' for _ in range(m)]
total = 0

for i in range(m):
    minCount = 987654321
    minNuc = 'X'

    for j in ['A', 'C', 'G', 'T']:
        count = 0

        for k in range(n):
            if dna[k][i] != j:
                count += 1

        if minCount > count:
            minCount = count
            minNuc = j

    total += minCount
    ans[i] = minNuc
    
print(''.join(ans))
print(total)
