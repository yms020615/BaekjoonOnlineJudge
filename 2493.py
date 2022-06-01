import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

stc = []
ans = [0] * n
for i in range(n):
    while stc and tower[stc[-1]] < tower[i]:
        stc.pop()
    if stc:
        ans[i] = stc[-1] + 1
    stc.append(i)

print(*ans)
