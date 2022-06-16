import sys
input = sys.stdin.readline

import math
x1, y1, a, x2, y2, b = map(float, input().split())

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if d >= a + b:
    s = 0

elif d <= abs(a - b):
    s = math.pi * (min(a, b) ** 2)
    
else:
    t1 = math.acos((a*a + d*d - b*b) / (2 * a * d)) * 2
    t2 = math.acos((b*b + d*d - a*a) / (2 * b * d)) * 2
    a1 = 0.5 * t2 * b*b - 0.5 * b*b * math.sin(t2)
    a2 = 0.5 * t1 * a*a - 0.5 * a*a * math.sin(t1)
    s = a1 + a2

print('%.3f' % s)
