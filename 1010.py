from math import comb

for i in range(int(input())):
    n, r = map(int, input().split())
    print(comb(max(n, r), min(n, r)))
