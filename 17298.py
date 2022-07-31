import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = [-1 for _ in range(n)]
stack = []
stack.append(0)
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        b[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
    i += 1
print(*b)
