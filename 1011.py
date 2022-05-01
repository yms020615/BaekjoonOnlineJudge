import math
for i in range(int(input())):
    a, b = map(int, input().split())
    x = 0
    y = b - a
    if y % math.sqrt(y) == 0:
        print(int(2 * math.sqrt(y)) - 1)
    elif (int(math.sqrt(y)) + int(math.sqrt(y)) + 1) / 2 > y:
        print(int(2 * math.sqrt(y)) + 1)
    elif (int(math.sqrt(y)) + int(math.sqrt(y)) + 1) / 2 < y:
        print(int(2 * math.sqrt(y)))
