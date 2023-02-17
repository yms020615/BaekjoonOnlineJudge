from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

d = deque([i for i in range(1, n+1)])

ans = 0
for i in a:
    while True:
        if i == d[0]:
            d.popleft()
            break
        else:
            if d.index(i) <= len(d) // 2:
                while i != d[0]:
                    d.append(d.popleft())
                    ans += 1
            else:
                while i != d[0]:
                    d.appendleft(d.pop())
                    ans += 1

print(ans)
