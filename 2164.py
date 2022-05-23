import sys
input = sys.stdin.readline

from collections import deque
a = deque()
n = int(input())
for i in range(n):
    a.append(i+1)
while len(a) > 1:
    a.popleft()
    a.append(a.popleft())
print(a[0])
