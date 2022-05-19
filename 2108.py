import sys
from collections import Counter
a = []
for _ in range(int(input())):
    a.append(int(sys.stdin.readline()))
mean = round(sum(a)/len(a))
a.sort()
median = a[len(a)//2]
scope = max(a) - min(a)
print(mean)
print(median)
b = Counter(a).most_common()
if len(b) > 1 and b[0][1] == b[1][1]:
    print(b[1][0])
else: print(b[0][0])
print(scope)
