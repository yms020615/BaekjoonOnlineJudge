input = __import__('sys').stdin.readline

from collections import deque

n, k = map(int, input().split())

ans = []
queue = deque([i for i in range(1, n + 1)])

count = 1
while queue:
    temp = []
    len_q = len(queue)
    inCount = 0

    while inCount < len_q:
        if count % k:
            temp.append(queue.popleft())
        else:
            ans.append(queue.popleft())
        count += 1
        inCount += 1

    queue = deque(temp)

print('<', end = '')
for i in ans:
    if i == ans[-1]:
        print('%d>' % i, end = '')
    else:
        print('%d,' % i, end = ' ')
