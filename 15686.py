import sys
input = sys.stdin.readline

from itertools import combinations
n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            house.append([i, j])
        elif s[i][j] == 2:
            chicken.append([i, j])
            s[i][j] = 0

comb = list(combinations(chicken, m))

minD = 9999999999

for i in range(len(comb)):
    dist = 0
    for j in range(n):
        for k in range(n):
            if s[j][k] == 1:
                temp = 9999999999
                for l in range(m):
                    temp = min(temp, abs(j - comb[i][l][0]) + abs(k - comb[i][l][1]))
                dist += temp
    minD = min(minD, dist)
print(minD)
