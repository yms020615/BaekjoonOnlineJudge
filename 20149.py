import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if temp > 0: return 1
    elif temp < 0: return -1
    else: return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            print(1)
            if min(x3, x4) == max(x1, x2) and min(y3, y4) == max(y1, y2):
                print(min(x3, x4), min(y3, y4))
            elif min(x1, x2) == max(x3, x4) and min(y1, y2) == max(y3, y4):
                print(min(x1, x2), min(y1, y2))
            else:
                if ccw(x1, y1, x2, y2, x4, y4) * ccw(x3, y3, x4, y4, x1, y1) != 0 or ccw(x1, y1, x2, y2, x3, y3) * ccw(x3, y3, x4, y4, x1, y1) != 0:
                    print(x2, y2)
                elif ccw(x1, y1, x2, y2, x4, y4) * ccw(x3, y3, x4, y4, x2, y2) != 0 or ccw(x1, y1, x2, y2, x3, y3) * ccw(x3, y3, x4, y4, x2, y2) != 0:
                    print(x1, y1)

        else:
            print(0)
    else:
        print(1)
        if x1 != x2 and x3 != x4:
            px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            print(px, py)
        elif x1 == x2 and x3 != x4:
            k = (y4-y3)/(x4-x3)
            print(x1, k*(x1-x3)+y3)
        elif x1 != x2 and x3 == x4:
            k = (y2-y1)/(x2-x1)
            print(x3, k*(x3-x1)+y1)

else:
    print(0)
