input = __import__('sys').stdin.readline

import math
n = int(input())
print(round(-1 + math.sqrt(1 + 8 * n) / 2 + 0.00001))
