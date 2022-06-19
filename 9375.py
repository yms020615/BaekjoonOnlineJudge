import sys
input = sys.stdin.readline

from collections import Counter
for i in range(int(input())):
    s = []
    n = 0
    for j in range(int(input())):
        a, b = input().split()
        s.append(b)
    k = 1
    r = Counter(s)
    for i in r:
        k *= r[i] + 1
    print(k-1)
