import sys
input = sys.stdin.readline

from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    index = [0 for _ in range(n)]
    index[m] = 1
    count = 0
    while True:
        if q[0] == max(q):
            if index[0] == 1:
                break
            else:
                q.popleft()
                index.pop(0)
                count += 1
        else:
            q.append(q.popleft())
            index.append(index.pop(0))
    print(count + 1)
