input = __import__('sys').stdin.readline

import math
import copy
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
p.sort()

def f(start, end):
    if end - start == 1:
        d = (p[start][0] - p[end][0]) ** 2 + (p[start][1] - p[end][1]) ** 2
        return d

    mid = (start + end) // 2
    d = min(f(start, mid), f(mid, end))

    q = []
    for i in range(start, end + 1):
        if (p[mid][0] - p[i][0]) ** 2 < d:
            q.append(p[i])
    q.sort(key = lambda x: x[1])

    for i in range(len(q) - 1):
        for j in range(i + 1, len(q)):
            if (q[j][1] - q[i][1]) ** 2 < d:
                d = min(d, (q[j][0] - q[i][0]) ** 2 + (q[j][1] - q[i][1]) ** 2)
            else:
                break

    return d

print(f(0, n - 1))
