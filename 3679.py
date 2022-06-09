import sys
input = sys.stdin.readline

import math
import heapq

def angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dx, dy)

def dist(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx ** 2 + dy ** 2)

n = int(input())
for _ in range(n):
    t = list(map(int, input().split()))
    point = []
    for i in range(t[0]):
        point.append([t[2*i + 1], t[2*i + 2], i])
    point.sort(key = lambda x: x[1])

    angles = {}
    min_angle = math.inf
    p0 = point[0]
    for i in point[1:]:
        d = angle(p0, i)
        min_angle = min(min_angle, d)
        angles[i[2]] = [d, dist(p0, i)]

    item = list(angles.items())
    item.sort(key = lambda x: (-x[1][0], x[1][1]))

    heap = []
    for i in item:
        if i[1][0] == min_angle:
            heapq.heappush(heap, [-i[1][1], i[0]])

    print(p0[2], end = ' ')
    for k, v in item[:-len(heap)]:
        print(k, end = ' ')
    while heap:
        print(heapq.heappop(heap)[1], end = ' ')
    print()
