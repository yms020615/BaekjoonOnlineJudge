input = __import__('sys').stdin.readline

n = int(input())

from heapq import *
heap1, heap2 = [], []
ans = []

for _ in range(n):
    temp = int(input())

    if len(heap1) == len(heap2):
        heappush(heap1, -temp)
    else:
        heappush(heap2, temp)

    if heap2 and -heap1[0] > heap2[0]:
        a, b = -heappop(heap1), heappop(heap2)
        heappush(heap1, -b)
        heappush(heap2, a)

    ans.append(-heap1[0])

for i in ans:
    print(i)
