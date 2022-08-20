input = __import__('sys').stdin.readline

n = int(input())
dasom = int(input())

if n == 1:
    print(0)
    exit(0)

from heapq import *

heap = []
for _ in range(n - 1):
    heappush(heap, -int(input()))

count = 0

while dasom <= -heap[0]:
    count += 1
    temp = -heappop(heap)

    dasom += 1
    temp -= 1

    heappush(heap, -temp)

print(count)
