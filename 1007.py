import sys
input = sys.stdin.readline

import math
from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    vect = []

    x_total = 0
    y_total = 0

    for _ in range(n):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        vect.append([x, y])

    ans = math.inf
    comb = list(combinations(vect, n // 2))
    for i in comb[:len(comb)//2]:
        i = list(i)

        x1_total = 0
        y1_total = 0
        for x1, y1 in i:
            x1_total += x1
            y1_total += y1

        x2_total = x_total - x1_total
        y2_total = y_total - y1_total
        ans = min(ans, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))

    print(ans)
