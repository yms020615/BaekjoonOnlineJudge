import sys
input = sys.stdin.readline

a = int(input())
m = sorted(map(int, input().split()))
b = int(input())
n = map(int, input().split())

from collections import Counter
s = Counter(m)
for i in n:
    if i not in s.keys():
        print(0, end=' ')
    else:
        print(s[i], end=' ')
