import sys
input = sys.stdin.readline

from collections import deque

while True:
    hist = deque(list(map(int, input().split())))
    n = hist.popleft()
    if n == 0 and not hist:
        break

    stack = []
    ans = 0
    for i in range(n):
        while stack and hist[stack[-1]] > hist[i]:
            check = stack.pop()

            if stack:
                ans = max(ans, hist[check] * (i - stack[-1] - 1))
            else:
                ans = max(ans, hist[check] * i)
        stack.append(i)

    while stack:
        temp = stack.pop()

        if stack:
            ans = max(ans, hist[temp] * (n - stack[-1] - 1))
        else:
            ans = max(ans, hist[temp] * n)

    print(ans)
