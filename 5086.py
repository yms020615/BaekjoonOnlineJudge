import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if not a and not b: break
    if a % b == 0: print('multiple')
    elif b % a == 0: print('factor')
    else: print('neither')
